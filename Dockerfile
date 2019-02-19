FROM ubuntu:xenial

ENV DEBIAN_FRONTEND noninteractive

COPY . /apt_tests
WORKDIR /apt_tests

RUN apt-get update && \
    apt-get install -y apt-utils build-essential python3-pip

RUN python3 -m pip install pip --upgrade && \
    python3 -m pip install wheel pipenv

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pipenv install
