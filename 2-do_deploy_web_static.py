#!/usr/bin/python3
# configure the website to the new release of the website """
import os
from fabric.api import run, put
from fabric.api import env
env.hosts = ['3.83.245.203', '54.173.35.201']


def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    if not os.path.isfile(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        dir_name = filename.split('.')[0]
        c_path = "/data/web_static/releases/"
        put(archive_path, f'/tmp/')
        run(f"mkdir -p {c_path}{dir_name}/")
        run(f"tar -xzf /tmp/{filename} -C {c_path}{dir_name}/")
        run(f"rm /tmp/{filename}")
        run(f"mv {c_path}{dir_name}/web_static/* {c_path}{dir_name}/")
        run(f"rm -rf {c_path}{dir_name}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {c_path}{dir_name}/ /data/web_static/current")
        return True
    except:
        return False
