#!/usr/bin/python3
# configure the website to the new release of the website

from fabric.api import run, put, env
import os
env.hosts = ['3.83.245.203', '54.173.35.201']


def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        c_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(c_path, dir_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, c_path, dir_name))
        run('rm /tmp/{}'.format(filename))
        run('mv {}{}/web_static/* {}{}/'.format(c_path, dir_name, c_path, dir_name))
        run('rm -rf {}{}/web_static'.format(c_path, dir_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(c_path, dir_name))
        return True
    except:
        return False

