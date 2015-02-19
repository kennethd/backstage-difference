#!/usr/bin/env python

# distutils does not support 'python setup.py develop'
#from distutils.core import setup
from setuptools import setup

setup(
    name = 'differencesvc',
    version = '0.1',
    description = 'example service implementation',
    author = 'Kenneth Dombrowski',
    author_email = 'kenneth@ylayali.net',
    url = 'http://git.ylayali.net/backstage-difference.git',
    packages = ['differencesvc', 'differencesvc.test'],
    license = 'MIT',
)

