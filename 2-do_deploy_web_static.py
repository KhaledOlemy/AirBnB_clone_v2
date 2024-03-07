#!/usr/bin/python3
"""
configure the website to the new release of the website 
"""

from fabric.api import run, put, env
import os
env.hosts = ['3.83.245.203', '54.173.35.201']


def do_deploy(archive_path):
    """ Deploy the content of the tar onto your servers"""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        d = f.split(".")[0]
        p = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(p, d))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f, p, d))
        run('rm /tmp/{}'.format(f))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(p, d))
        run('rm -rf {}{}/web_static'.format(p, d))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(p, d))
        return True
    except:
        return False
