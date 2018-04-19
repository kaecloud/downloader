#!/bin/sh

echo "[Credentials]" > /root/.ossutilconfig
echo "language=EN" >> /root/.ossutilconfig
echo "endpoint=$OSS_ENDPOINT" >> /root/.ossutilconfig
echo "accessKeyID=$OSS_ID" >> /root/.ossutilconfig
echo "accessKeySecret=$OSS_KEY" >> /root/.ossutilconfig

exec "$@"
