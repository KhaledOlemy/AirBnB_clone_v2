#!/usr/bin/python3
""" Compress a folder and return path to .tgz """
import os
from fabric.api import run, put
from fabric.api import env
env.hosts = ['3.83.245.203', '54.173.35.201']

def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    filename = archive_path.split('/')[-1]
    extract_dest = '/'.join(archive_path.split('/')[:-1])
    dir_name = filename.split('.')[0]
    if not os.path.isfile(archive_path):
        return False
    if put(archive_path, f'/tmp/{filename}').failed:
        return False
    if run(f"rm -r /data/web_static/releases/{dir_name}").failed:
        return False
    if run(f"mkdir -p /data/web_static/releases/{dir_name}").failed:
        return False
    if run(f"tar -xvzf /tmp/{filename} -C /data/web_static/releases/{dir_name}").failed:
        return False
    if run(f"mv /data/web_static/releases/{dir_name}/web_static/* /data/web_static/releases/{dir_name}").failed:
        return False
    if run(f"rm -r /data/web_static/releases/{dir_name}/web_static").failed:
        return False
    if run(f"rm /tmp/{filename}").failed:
        return False
    if run(f"rm /data/web_static/current").failed:
        return False
    if run(f"ln -sf /data/web_static/releases/{dir_name} /data/web_static/current").failed:
        return False
    return True
