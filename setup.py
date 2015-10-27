#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Sosuke Kato <snoopies.drum@gmail.com>
#
# License: MIT

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DISTNAME = "cornel-movie-dialogs-corpus-storm"
DESCRIPTION = "A set of python modules for cornel movie-dialogs corpus with storm"
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()
URL = "http://sosuke-k.github.io/mdcorpus"
LICENSE = "MIT"
# PY_MODULES = ["mdcorpus"]
PACKAGES = ["mdcorpus"]
PACKAGE_DIR = {"mdcorpus": "mdcorpus"}

import mdcorpus
VERSION = mdcorpus.__version__


def setup_package():
    metadata = dict(name=DISTNAME,
                    description=DESCRIPTION,
                    license=LICENSE,
                    url=URL,
                    version=VERSION,
                    long_description=LONG_DESCRIPTION,
                    # py_modules=PY_MODULES,
                    packages=PACKAGES,
                    package_dir=PACKAGE_DIR,
                    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
