FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN whereis python3
RUN whereis pip
#RUN export PYTHONPATH="${PYTHONPATH}:/usr/bin/python3.8"

CMD python3 --version
ADD prereq.txt  /storage/

RUN pip3 install -r /storage/prereq.txt

WORKDIR /storage

EXPOSE 8000

ADD entrypoint.sh               /storage/
ADD manager.specs.yaml          /storage/
ADD manager/*.py                /storage/manager/