FROM ipanousis/armada-docker-register
MAINTAINER Yannis Panousis ipanousis156@gmail.com

RUN apt-get install -y python-pip libffi-dev libssl-dev
RUN pip install python-etcd

ADD . /app

ENV NOTIFY python /app/etcd-register.py
