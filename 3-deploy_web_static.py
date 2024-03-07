#!/usr/bin/python3
""" Compress a folder and return path to .tgz """
import datetime
import os
from fabric.api import local, run, put, env

env.hosts = ['3.83.245.203', '54.173.35.201']


def do_pack():
    """
    Pack dir to .tgz
    """
    filename = str(datetime.datetime.now()).split('.')[0].replace('-', '')
    filename = filename.replace(' ', '').replace(':', '')
    filename = f"versions/web_static_{filename}.tgz"
    if not os.path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    status = local(f"tar -cvzf {filename} web_static")
    if status.failed:
        return None
    else:
        return filename


def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    if not os.path.isfile(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    dir_name = filename.split('.')[0]
    if put(archive_path, f'/tmp/{filename}').failed:
        return False
    if run(f"mkdir -p /data/web_static/releases/{dir_name}/").failed:
        return False
    d1 = f"/data/web_static/releases/{dir_name}/"
    if run(f"tar -xzf /tmp/{filename} -C {d1}").failed:
        return False
    if run(f"rm /tmp/{filename}").failed:
        return False
    d1 = f"/data/web_static/releases/{dir_name}/web_static/*"
    d2 = f"/data/web_static/releases/{dir_name}/"
    if run(f"mv {d1} {d2}").failed:
        return False
    if run(f"rm -rf /data/web_static/releases/{dir_name}/web_static").failed:
        return False
    if run(f"rm -rf /data/web_static/current").failed:
        return False
    d1 = f"/data/web_static/releases/{dir_name}/"
    d2 = f"/data/web_static/current"
    if run(f"ln -s {d1} {d2}").failed:
        return False
    print("New version deployed!")
    return True


f = do_pack()


def deploy():
    """2 calls at once, more automated"""
    if not f:
        return False
    return do_deploy(f)
