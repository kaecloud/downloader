FROM alpine:latest

ADD http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/50452/cn_zh/1516453988016/ossutil32 /usr/bin/ossutil
RUN chmod a+x /usr/bin/ossutil

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
