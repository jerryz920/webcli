#!/usr/bin/env python
from flask import Blueprint
import subprocess

# this could be installed together with a pio-template code inside Docker
# container. The template code path is pointed to /opt/pio/ by default.
# FIXME: make it configurable later

mapper = Blueprint('pio-mgmt-api', __name__)
script_home = "/var/lib/webcli/scripts/pio/"

@mapper.route("/pio/start")
def start():
    return subprocess.check_output(script_home + "start.sh")

@mapper.route("/pio/stop")
def stop():
    return subprocess.check_output(script_home + "stop.sh")

@mapper.route("/pio/build")
def build():
    return subprocess.check_output(script_home + "build.sh")

@mapper.route("/pio/train")
def train():
    return subprocess.check_output(script_home + "train.sh")

@mapper.route("/pio/deploy")
def deploy():
    return subprocess.check_output(script_home + "deploy.sh")

@mapper.route("/pio/show")
def show():
    return subprocess.check_output(script_home + "show.sh")
