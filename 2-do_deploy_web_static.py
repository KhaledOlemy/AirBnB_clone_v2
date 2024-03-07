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
        put(archive_path, f'/tmp/{filename}')
        run(f"mkdir -p /data/web_static/releases/{dir_name}/")
        d1 = f"/data/web_static/releases/{dir_name}/"
        run(f"tar -xzf /tmp/{filename} -C {d1}")
        run(f"rm /tmp/{filename}")
        d1 = f"/data/web_static/releases/{dir_name}/web_static/*"
        d2 = f"/data/web_static/releases/{dir_name}/"
        run(f"mv {d1} {d2}")
        run(f"rm -rf /data/web_static/releases/{dir_name}/web_static")
        run(f"rm -rf /data/web_static/current")
        d1 = f"/data/web_static/releases/{dir_name}/"
        d2 = f"/data/web_static/current"
        run(f"ln -s {d1} {d2}")
        print("New version deployed!")
        return True
    except:
        return False
