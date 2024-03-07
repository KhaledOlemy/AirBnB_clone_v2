#!/usr/bin/python3
# Compress a folder and return path to .tgz
import datetime
import os
import fabric


def do_pack():
    filename = str(datetime.datetime.now()).split('.')[0].replace('-', '')
    filename = filename.replace(' ', '').replace(':', '')
    filename = f"web_static_{filename}.tgz"
    print(filename)
    local = fabric.api.local
    if not os.path.isdir("versions"):
        status = local("mkdir versions").succeeded
        print(status)
        if not status:
            return None
    status = local(f"tar -czvf versions/{filename} web_static")
    status = status.succeeded
    print(status)
    if not status:
        return None
    else:
        return f"versions/{filename}.tgz"
