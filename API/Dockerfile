FROM amd64/centos:latest

RUN yum update -y && yum install -y python3.8 \
    python3-pip \
    && \
    rm -rf /var/lib/apt/lists/*

ADD prereq.txt  /storage/

RUN pip3 install -r /storage/prereq.txt

WORKDIR /storage

EXPOSE 8000

ADD entrypoint.sh               /storage/
ADD manager.specs.yaml          /storage/
ADD manager/*.py                /storage/manager/