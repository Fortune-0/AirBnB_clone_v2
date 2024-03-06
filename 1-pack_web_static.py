#!/usr/bin/python3
"""1. Compress before sending"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    # getting time and formating it
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    # naming the file
    name = "web_static_{}.tgz".format(time)

    # command
    comm = "tar -cvzf versions/{} web_static/".format(name)

    # execution
    local('mkdir -p versions/')
    path = local(comm)
    if path.succeeded:
        return "versions/{}".format(name)
