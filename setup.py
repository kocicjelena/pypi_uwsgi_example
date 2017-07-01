#!/usr/bin/python
import os
import sys
from io import open
from setuptools import setup
from distutils.core import setup, Extension

files = ["pypiuwsgiexample"]
setup(name='pypiuwsgiexample',
      packages=['pypiuwsgiexample'],
	  package_dir={'pypiuwsgiexample': 'pypiuwsgiexample'},
      version='1.0',
      description='uwsgi example',
      author='Jelena',
      author_email='kocicjelena@gmail.com',
	  include_package_data=True,
	  url='https://github.com/kocicjelena/py/',
	  scripts = ["run"],
	  install_requires=[
               'uWSGI',
	       'Flask'
    ]
	)
