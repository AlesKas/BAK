FROM ubuntu:18.04 as base

RUN apt-get update -y 
RUN apt-get install -y python3.8
RUN python3.8 --version
RUN apt-get install -y python3-pip
RUN rm -rf /var/lib/apt/lists/

#ENV LANG en_US.UTF-8
#ENV LC_ALL en_US.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
#RUN dpkg-reconfigure locales
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV FLASK_APP manager.main

WORKDIR /storage

ADD Pipfile  /storage/

RUN export PIPENV_USE_SYSTEM=1
RUN pip3 install --upgrade pipenv
RUN pipenv lock
RUN pipenv install --ignore-pipfile --deploy --system
RUN ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 8000
EXPOSE 5678

ADD entrypoint.sh               /storage/
ADD manager.specs.yaml          /storage/
ADD manager/*.py                /storage/manager/
ADD utils/db/*.py               /storage/utils/db/
ADD utils/*.py                  /storage/utils/     
