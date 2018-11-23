FROM alpine:latest

ADD http://gosspublic.alicdn.com/ossutil/1.4.2/ossutil32 /usr/bin/ossutil
RUN chmod a+x /usr/bin/ossutil

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
