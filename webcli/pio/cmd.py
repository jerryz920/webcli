#!/usr/bin/env python
from flask import Blueprint

# this could be installed together with a pio-template code inside Docker
# container. The template code path is pointed to /opt/pio/ by default.
# FIXME: make it configurable later

mapper = Blueprint('pio-mgmt-api', __name__)

@mapper.route("/pio/new")
def create():
    return "this is a test"

@mapper.route("/pio/delete")
def delete():
    return "delete the app"

@mapper.route("/pio/build")
def build():
    return "build app"

@mapper.route("/pio/train")
def train():
    return "build app"

@mapper.route("/pio/serve")
def train():
    return "build app"
