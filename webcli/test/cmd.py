#!/usr/bin/env python
from flask import Blueprint

mapper = Blueprint('testapi', __name__)


@mapper.route("/test")
def print_test():
    return "this is a test"
