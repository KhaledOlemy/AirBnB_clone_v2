#!/usr/bin/python3
# Compress a folder and return path to .tgz
import datetime
import os
from fabric.api import local


def do_pack():
    filename = str(datetime.datetime.now()).split('.')[0].replace('-', '')
    filename = filename.replace(' ', '').replace(':', '')
    filename = f"versions/web_static_{filename}.tgz"
    if not os.path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    status = local(f"tar -czvf {filename} web_static")
    if status.failed:
        return None
    else:
        return filename
