#!/usr/bin/env python

"""
========
setup.py
========

Installs {{cookiecutter.repo_name}}

DEV only:

git commit -am "version bump";git push origin master
git tag -a v$(python setup.py --version) -m "Update";git push --tags
"""
import sys
try:
    from setuptools import setup, find_packages, Extension
except ImportError:
    from distutils.core import setup, find_packages, Extension

with open('requirements.txt') as f:
    required = f.read().splitlines()

# main setup
setup(
name='{{cookiecutter.repo_name}}',
author='{{cookiecutter.author_name}}',
author_email='{{cookiecutter.author_email}}',
version='0.0.0',
url='https://github.com/{{cookiecutter.author_username}}/{{cookiecutter.repo_name}}',
download_url='https://github.com/{{cookiecutter.author_username}}/{{cookiecutter.repo_name}}/archive/master.zip',
description='{{cookiecutter.repo_name}} project',
long_description='https://github.com/{{cookiecutter.author_username}}/{{cookiecutter.repo_name}}/README.md',
# keywords=['','',''],
license='General Public License v. 3',
install_requires=required,
platforms='Tested on Ubuntu 16.04 64bit',
packages=find_packages(exclude=['test*', 'deps*', 'data*', 'data']),
include_package_data=True,
entry_points={
    'console_scripts': ['template = template.run:parser.dispatch',],
    },
)
