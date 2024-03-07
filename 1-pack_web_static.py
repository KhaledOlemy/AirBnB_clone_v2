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
        if not local("mkdir versions").succeeded:
            return None
    status = local(f"tar -czvf versions/{filename} web_static")
    if not status.succeeded:
        return None
    else:
        return f"versions/{filename}"
