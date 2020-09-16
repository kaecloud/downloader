FROM python:3.7-slim-stretch

RUN sed -i 's/deb.debian.org/mirrors.163.com/g' /etc/apt/sources.list && \
  sed -i 's/security.debian.org/mirrors.163.com/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y git wget unzip

ADD http://gosspublic.alicdn.com/ossutil/1.6.18/ossutil64 /usr/bin/ossutil
RUN chmod a+x /usr/bin/ossutil

COPY entrypoint.py /
ENTRYPOINT ["/entrypoint.py"]
