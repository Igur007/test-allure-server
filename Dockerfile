# Python 3.10.6 + allure + test harness
FROM python:3.10.6

ENV PROJECT_LOCATION /app
RUN mkdir -p $PROJECT_LOCATION
WORKDIR $PROJECT_LOCATION

# Allure args
ARG allure_version=2.19.0
ARG allure_download_link=https://github.com/allure-framework/allure2/releases/download/${allure_version}/allure-${allure_version}.tgz

RUN apt-get update -qq && \
    apt-get install -y software-properties-common && \
    apt-get install -y default-jre

# Install Allure
RUN curl -o allure-${allure_version}.tgz -Ls ${allure_download_link} && \
    tar -zxvf allure-${allure_version}.tgz -C /opt/ && \
    ln -s /opt/allure-${allure_version}/bin/allure /usr/bin/allure

RUN pip install --no-cache-dir --upgrade poetry invoke
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true

ADD . $PROJECT_LOCATION
RUN inv install

RUN rm -rf etc /tmp/* /root/.ssh /root/.cache

# Need a mounted volume to get allure back out?
# CMD poetry run pytest tests/integration -x -s
