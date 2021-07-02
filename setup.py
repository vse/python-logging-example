#!/usr/bin/env python

from distutils.core import setup

setup(name='logger_example',
      version='0.1',
      description='Example for the logging configuration',
      packages=['testcmd'],
      entry_points = {
        'console_scripts': ['testcmd=testcmd.__main__:main'],
      }
     )
