#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['3.83.245.203', '54.173.35.201']


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
        run('mv {}{}/web_static/* {}{}/'.
            format(cmn_path, dir_name, cmn_path, dir_name))
        run('rm -rf {}{}/web_static'.format(cmn_path, dir_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(cmn_path, dir_name))
        print("New version deployed!")
        return True
    except:
        return False


f = do_pack()


def deploy():
    """2 calls at once, more automated"""
    if not f:
        return False
    return do_deploy(f)
