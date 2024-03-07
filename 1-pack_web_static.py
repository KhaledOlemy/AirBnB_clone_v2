#!/usr/bin/python3
# Compress a folder and return path to .tgz
import datetime
import os.path
from fabric.api import local


def do_pack():
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if not os.path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    status = local(f"tar -cvzf {filename} web_static")
    if status.failed:
        return None
    else:
        return filename
