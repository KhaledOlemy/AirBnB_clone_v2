#!/usr/bin/python3
"""
compress files into .tgz to be later deployed on servers
"""

import datetime
from fabric.api import local
import os


def do_pack():
    """compress static into .tgz"""
    try:
        fname = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        if not os.path.isdir("versions"):
            local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(fname)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return False
