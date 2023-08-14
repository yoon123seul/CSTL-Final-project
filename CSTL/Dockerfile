FROM ubuntu:18.04
MAINTAINER lim, min teak

RUN apt-get update
RUN apt-get install -y software-properties-common
#RUN add-apt-repository -y ppa:fkrull/deadsnakes
#RUN apt-get update
RUN apt-get install -y --no-install-recommends python3.6 python3.6-dev python3-pip python3-setuptools python3-wheel gcc
#RUN apt-get install -y git

RUN python3.6 -m pip install pip --upgrade
RUN pip install kafka-python

RUN apt-get install -y iputils-ping
RUN apt-get install -y net-tools
RUN apt-get install -y tcpdump
RUN apt-get install -y vim
RUN apt-get install -y git


#Install Oracle JAVA
RUN  mkdir -p /opt
ADD jdk-8u172-linux-x64.tar.gz /opt

#Configurate environmental variables
ENV JAVA_HOME /opt/jdk
ENV PATH $PATH:/opt/jdk/bin
RUN ln -s `ls /opt | grep "^jdk.*"` /opt/jdk && ln -s /opt/jdk/bin/java /usr/local/bin/java

#this
#RUN mkdir -p /kafka
#WORKDIR /kafka

COPY kafka_2.12-2.4.0 /kafka
WORKDIR /kafka
COPY producer.py /kafka/producer.py
COPY consumer.py /kafka/consumer.py
WORKDIR /kafka
#CMD ["python3.6", "producer.py"]


