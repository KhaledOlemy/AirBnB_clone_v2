#!/usr/bin/python3
""" configure the website to the new release of the website """
import os
from fabric.api import run, put
from fabric.api import env
env.hosts = ['3.83.245.203', '54.173.35.201']


def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    if not os.path.isfile(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    extract_dest = '/'.join(archive_path.split('/')[:-1])
    dir_name = filename.split('.')[0]
    if put(archive_path, f'/tmp/{filename}').failed:
        return False
    if run(f"rm -rf /data/web_static/releases/{dir_name}").failed:#
        return False
    if run(f"mkdir -p /data/web_static/releases/{dir_name}").failed:
        return False
    d1 = f"/data/web_static/releases/{dir_name}"#
    if run(f"tar -xzf /tmp/{filename} -C {d1}").failed:#
        return False
    d1 = f"/data/web_static/releases/{dir_name}/web_static/*"
    d2 = f"/data/web_static/releases/{dir_name}"
    if run(f"mv {d1} {d2}").failed:
        return False
    if run(f"rm -rf /data/web_static/releases/{dir_name}/web_static").failed:#
        return False
    if run(f"rm /tmp/{filename}").failed:
        return False
    if run(f"rm -rf /data/web_static/current").failed:#
        return False
    d1 = f"/data/web_static/releases/{dir_name}"#
    d2 = f"/data/web_static/current"
    if run(f"ln -sf {d1} {d2}").failed:
        return False
    return True
