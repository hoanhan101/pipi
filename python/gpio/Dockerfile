FROM resin/rpi-raspbian:latest

MAINTAINER Hoanh An "hoanhan@bennington.edu"

RUN apt-get -q update && \
    apt-get -qy install \
    python python-pip \
    python-dev python-pip gcc make  

RUN pip install rpi.gpio
