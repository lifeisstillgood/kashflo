#!/usr/bin/env python
#! -*- coding: utf-8 -*-

###
# Copyright (c) Paul Brian 2013
# This software is subject to
# the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
###


"""
setup for HomeSpendWatch


"""

from setuptools import setup, find_packages
import os, glob

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()



def get_version():
    """ return a version number, or error string.
    
    We are assuming a file version.txt always exists. By convention
    populate that file with output of git describe
    """

    try:
        v = open("version.txt").read().strip()
    except:
        v = "UNABLE_TO_FIND_RELEASE_VERSION_FILE"
    return v



setup(
    name='homespendwatch',
    version=get_version(),
    packages=find_packages(),
    author='See AUTHORS.txt',
    author_email='paul@mikadosoftware.com',
    long_description=README,
    license='LICENSE.txt',
    description="Simple Home Accounts spending tracker "\
                "to work with any bank",
    entry_points = """\
    [console_scripts]
    homespendwatch-run = homespendwatch.run:main
    """,
    )
