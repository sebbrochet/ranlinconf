#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.abspath('lib'))
from ranlinconf import __version__, __author__
from distutils.core import setup

setup(name='ranlinconf',
      version=__version__,
      description='Linux configuration changes tracker',
      long_description='This command-line tool lets you track remotely configuration changes made to a list of linux servers between successive runs. You get a mail for each server change with the details of the change.',
      author=__author__,
      author_email='contact@sebbrochet.com',
      url='https://code.google.com/p/ranlinconf/',
      platforms=['linux'],
      license='MIT License',
      install_requires=['paramiko'],
      package_dir={ 'ranlinconf': 'lib/ranlinconf' },
      packages=[
         'ranlinconf',
      ],
      scripts=[
         'bin/ranlinconf',
         'bin/list_linconf'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: System :: Monitoring',
          ],
      )