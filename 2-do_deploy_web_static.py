#!/usr/bin/python3
"""2. Deploy archive!"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["18.204.9.96", "54.144.144.63"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to the web servers""" 
    if not os.path.exists(archive_path):
        return False
    try:
        # getting name of archive from archive_path
        temp = str(archive_path).split("/")[-1]
        name = temp.split(".")[0]
        
        # placing the archive
        put(archive_path, "/tmp/")

        # uncompressing...
        # extraction path
        extrPath = "/data/web_static/releases/{}/".format(name)
        run("sudo mkdir -p {}".format(extrPath))
        run("sudo tar -xzf /tmp/{} -C {}".format(temp, extrPath))
        run("sudo mv {}/web_static/* {}".format(extrPath, extrPath))
        # removing extracted
        run("sudo rm /tmp/{}".format(temp))

        # deletes the symbolic
        run("sudo rm -rf /data/web_static/current")

        # new symbolic link
        run("sudo ln -s {} /data/web_static/current".format(extrPath))
        return True
    except Exception:
        return False
