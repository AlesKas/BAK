FROM amd64/centos:latest as base

RUN yum update -y && \
    yum install -y which && \
    yum install -y python3.8 \
    python3-pip \
    && \
    rm -rf /var/lib/apt/lists/*
RUN yum remove -y python3

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /storage

ADD Pipfile*  /storage/

RUN export PIPENV_USE_SYSTEM=1
RUN pip3 install --upgrade pipenv && \
    pipenv install --ignore-pipfile --deploy --system && ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 8000

ADD entrypoint.sh               /storage/
ADD manager.specs.yaml          /storage/
ADD manager/*.py                /storage/manager/
ADD utils/db/*.py               /storage/utils/db/
ADD utils/*.py                  /storage/utils/