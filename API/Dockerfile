FROM python:3.8-slim-buster
# RUN apt update
# RUN apt install software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt update
# RUN apt install python3.8

RUN python --version

ADD prereq.txt  /storage/

#ADD /Pipfile * /storage/

# RUN pip3 install --upgrade pipenv && \
#     pipenv install
RUN pip install -r /storage/prereq.txt

WORKDIR /storage/


ADD entrypoint.sh   /storage/

ADD manager/*.py    /storage/manager/