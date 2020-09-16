#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""

"""
from __future__ import print_function, division, absolute_import
import sys
import os
import json
import shlex
import subprocess


def prepare_oss_config():
    key_id = os.getenv("OSS_ID")
    key_secret = os.getenv("OSS_SECRET")
    endpoint = os.getenv("OSS_ENDPOINT")
    if key_id is None:
        raise ValueError("OSS_ID environment variable is needed")
    if key_secret is None:
        raise ValueError("OSS_SECRET environment variable is needed")
    if endpoint is None:
        raise ValueError("OSS_ENDPOINT environment variable is needed")

    ss = f"""
[Credentials]
language=EN
endpoint={endpoint}
accessKeyID={key_id}
accessKeySecret={key_secret}"""
    oss_cfg_name = os.path.expanduser("~/.ossutilconfig")
    with open(oss_cfg_name, "w") as fp:
        fp.write(ss)


def run_cmd(cmd):
    cmd_list = shlex.split(cmd)
    res = subprocess.run(cmd_list, shell=False, check=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
    )
    if res.returncode != 0:
        print(res.stderr.decode("utf8"))
    print(res.stdout.decode("utf8"))
    res.check_returncode()


def download_file(url, local_filename):
    lower_url = url.lower()
    if lower_url.startswith("oss:"):
        print(f"===== OSS: downloading {url}")
        cfg_name = os.path.expanduser("~/.ossutilconfig")
        dest_name = local_filename
        if lower_url.endswith(".zip") and (not dest_name.endswith(".zip")):
            dest_name += ".zip"
        run_cmd(f"ossutil cp {url} {dest_name} --config-file {cfg_name}")
        run_cmd(f"unzip {dest_name}")
    elif lower_url.startswith("http:") or lower_url.startswith("https:"):
        print(f"===== WGET: downloading {url} to {local_filename}")
        run_cmd(f"wget {url} -O {local_filename}")
    else:
        print(f"Can't downlod {url}")
        sys.exit(1)


if __name__ == "__main__":
    prepare_oss_config()
    if len(sys.argv) != 2:
        print("you should specify one argument")
    artifacts = json.loads(sys.argv[1])
    for artifact in artifacts:
        download_file(artifact['url'], artifact['local'])
