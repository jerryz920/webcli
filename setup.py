import os
from setuptools import  setup, find_packages
import subprocess

setup(
        name = "webcli",
        version = "0.1.0",
        author = "Yan Zhai",
        author_email = "zhaiyan920@gmail.com",
        description = "a set of management tool for local commands",
        license = "BSD",
        packages=find_packages(),
        scripts=["bin/mgmt-proxy"]
        )

# install scripts
os.mkdir("/var/lib/webcli", 0755)
subprocess.call(["cp", "-r", "scripts", "/var/lib/webcli"])



