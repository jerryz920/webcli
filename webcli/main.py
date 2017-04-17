#!/usr/bin/env python
from flask import Flask
import importlib
import sys
import optparse
import time
import os

app = Flask(__name__)
cmdproxy = "default"

@app.route("/")
def print_help():
    return "mgmt proxy for %s" % cmdproxy

def main():
    # personal preference for 1987
    if len(sys.argv) >= 2:
        cmdproxy = sys.argv[1]
        __import__("webcli.test")
        proxy_mod = importlib.import_module("webcli." + cmdproxy)
        proxy_mod.init(app)
    app.run(host='0.0.0.0', port=1987, debug=False)
