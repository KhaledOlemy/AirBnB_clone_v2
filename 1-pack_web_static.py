#!/usr/bin/python3
# Compress a folder and return path to .tgz
import datetime
import os
from fabric.api import local


def do_pack():
    filename = str(datetime.datetime.now()).split('.')[0].replace('-', '')
    filename = filename.replace(' ', '').replace(':', '')
    filename = f"web_static_{filename}.tgz"
    if not os.path.isdir("versions"):
        status = local("mkdir versions").succeeded
        if not status:
            return None
    status = local(f"tar -czvf versions/{filename} web_static")
    status = status.succeeded
    if not status:
        return None
    else:
        return f"versions/{filename}.tgz"
