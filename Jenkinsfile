pipeline {
    environment {
        registryCredential = 'dockerpush'
        dockerhubCredential = 'dockerhub'
        jfrogRegistryCredential = 'jfrog_docker'
        jfrogURL = 'https://xxxx.jfrog.io'
        JFROG_TOKEN = credentials('JFROG_TOKEN')
        dockerImage = ''
        VERSION = sh(returnStdout: true, script: "cat harness/__init__.py | sed 's/^.*__version__ = \"\\([^\"]*\\).*/\\1/'").trim()
    }
    agent {
        kubernetes {
            inheritFrom 'core-tests' // all pods will be named with this prefix
            // idleMinutes 5  // how long the pod will live idle
            yamlFile '.build-pod.yaml' // path to the pod definition relative to the root
            defaultContainer 'dind' // define a default container - will default to jnlp container
        }
    }
    stages {
        stage('Build') {
            options {
               retry(2)
            }
            steps {
                container("dind") {
//                     }
                script {
                        docker.withRegistry('', dockerhubCredential ) {
                            sh "docker rm -f python-allure || true" // delete container "python-allure" and don't return error if it does not exist
                            sh "docker build -t python-allure:$BUILD_NUMBER . && docker run -d --rm --name python-allure -v \$(pwd):/app python-allure:$BUILD_NUMBER sleep infinity" // build image and run new python-allure container with all current content mounted to /app inside
                            sh "docker exec -i python-allure bash -ce \"pip install --no-cache-dir --upgrade poetry invoke\""
                            sh "docker exec -i python-allure bash -ce \"poetry config virtualenvs.create true && poetry config virtualenvs.in-project true && inv install-dev\""
                            sh "docker exec -i python-allure bash -ce \"source /app/.venv/bin/activate && inv check-style && inv tests-coverage\""
                        }
                    }
                }
            }
        }
        stage('Test') {
            when {
                branch "main"
            }
            steps {
                container("dind") {
                    script {
                        docker.withRegistry('', dockerhubCredential ) {
                            sh "docker exec -i python-allure bash -ce \"source /app/.venv/bin/activate && inv tests-cluster\""
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            container("dind") {
                allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [[key: 'allure.issues.tracker.pattern', value: 'https://xxx.atlassian.net/browse/%s']],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: './allure-results']]
                ])
            }
        }
    }
}
