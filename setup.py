#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='Distutils',
      version='1.0',
      description='Usage Data Uplight',
      author='haris tanvir',
      test_suite='nose.collector',
      packages=find_packages(),
      install_requires=['click']
      )
