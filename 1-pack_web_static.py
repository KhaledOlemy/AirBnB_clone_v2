#!/usr/bin/python3
"""
Compress a folder and return path to .tgz
"""
import datetime
import os
from fabric.api import local


def do_pack():
    """
    Pack dir to .tgz
    """
    try:
    	filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    	filename = f"versions/web_static_{filename}.tgz"
        if not os.path.isdir("versions"):
            local("mkdir versions")
        local(f"tar -cvzf {filename} web_static")
        return filename
    except:
        return None

