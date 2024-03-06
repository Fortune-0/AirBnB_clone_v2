#!/usr/bin/python3
"""2. Deploy archive!"""
from fabric.api import *
import os



def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    env.hosts = ["18.204.9.96", "54.144.144.63"]
    env.user = "ubuntu"
    if not os.path.exists(archive_path):
        return False
    try:
        # placing the archive
        put(archive_path, "/tmp/")

        # getting name of archive from archive_path
        temp = str(archive_path).split("/")[-1]
        name = temp.split(".")[0]

        # uncompressing...
        # extraction path
        extrPath = "/data/web_static/releases/{}/".format(name)
        run("mkdir -p {}".format(extrPath))
        run("tar -xzf /tmp/{} -C {}".format(temp, extrPath))
        # removing extracted
        run("rm /tmp/{}".format(temp))

        # deletes the symbolic
        run("rm -rf /data/web_static/current")

        # new symbolic link
        run("ln -s {} /data/web_static/current".format(extrPath))
        return True
    except:
        return False
