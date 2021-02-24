FROM ubuntu:18.04 as base

RUN apt-get update -y 
RUN apt-get install -y libpq-dev
RUN apt remove -y python3.6
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.8-dev
RUN rm -rf /var/lib/apt/lists/

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
RUN rm /usr/bin/python3
RUN ln -s python3.8 /usr/bin/python3

RUN python3 -V

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV FLASK_APP manager.main

WORKDIR /storage

RUN python3 --version

ADD Pipfile*  /storage/

RUN export PIPENV_USE_SYSTEM=1
RUN pip3 install --upgrade pipenv
RUN pipenv install --ignore-pipfile --deploy --system
RUN pip3 install psycopg2
RUN ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 8000
EXPOSE 5678

ADD entrypoint.sh               /storage/
ADD manager.specs.yaml          /storage/
ADD manager/*.py                /storage/manager/
ADD utils/db/*.py               /storage/utils/db/
ADD utils/*.py                  /storage/utils/     
