#!/usr/bin/python3
"""
configure the website to the new release of the website
configure the website to the new release of the website
"""

from fabric.api import put, run, env
from os.path import isfile
env.hosts = ['3.83.245.203', '54.173.35.201']


def do_deploy(archive_path):
    """configure the website to the new release of the website"""
    if isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        dir_name = file_name.split(".")[0]
        cmn_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(cmn_path, dir_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, cmn_path, dir_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}{}/web_static/* {}{}/'.format(cmn_path, dir_name, cmn_path, dir_name))
        run('rm -rf {}{}/web_static'.format(cmn_path, dir_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(cmn_path, dir_name))
        print("New version deployed!")
        return True
    except:
        return False
