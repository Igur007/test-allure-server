# Repository with QA autotests. v0.0.1

# Setup

1. [Install brew](https://www.ruby-lang.org/en/documentation/installation/)
   e.g. on Mac:
   `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
2. [Install Python 3.10+](https://www.python.org/downloads/). Also it's possible to install with brew:

   `brew install python@3.10`

   or use pyenv to manage versions
3. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

   E.g. with pip `pip3.10 install uv`
4. Install dependencies

   `uv sync --extra dev`

   `uv run pre-commit install`

# Reporting

1. [Install allure](https://docs.qameta.io/allure/#_get_started).

   E.g. with brew:

   `brew install allure`
2. Generate views:

   `allure generate {path_to_results_folder} --clean`
3. Open reports:

   `allure open`

Note: tests should run with ```--alluredir {path_to_results_folder}``` to create allure results, e.g.
```--alluredir ./allure-results```

# UI autotests setup docker
1. [Install selenoid](https://aerokube.com/selenoid/latest/#_getting_started)

   E.g.:

   `curl -s https://aerokube.com/cm/bash | bash \
   && ./cm selenoid start --vnc --tmpfs 128`
2. [Start selenoid](https://aerokube.com/selenoid/latest/#_start_selenoid)

   E.g. with docker:

   `docker run -d                                   \
   --name selenoid                                 \
   -p 4444:4444                                    \
   -v /var/run/docker.sock:/var/run/docker.sock    \
   -v `pwd`/config/:/etc/selenoid/:ro              \
   aerokube/selenoid:latest-release`
3. [Start selenoid UI](https://aerokube.com/selenoid-ui/latest/#_quick_start_guide)
   E.g. with docker:

   `docker run -d --name selenoid-ui  \
   --link selenoid                 \
   -p 8082:8080                    \
   aerokube/selenoid-ui --selenoid-uri=http://selenoid:4444`
4. Open in browser [selenoid UI](http://localhost:8082/#/)
5. If is needed pull docker browser images.

   E.g.: `docker pull selenoid/vnc:firefox_57.0`

## Code Quality

### Tests

```bash
invoke tests
invoke tests-coverage
```

## Linting

```bash
invoke check-style
invoke isort
```

## Releases

Release management is handled using `bump2version`. The below commands will tag
a new release. This will also update the helm chart version, this should not be
manually changed.

```bash
$ invoke bump-patch
$ invoke bump-minor
$ invoke bump-major
> vX.Y.Z
```
