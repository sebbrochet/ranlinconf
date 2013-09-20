## ranlinconf: Track changes of the configuration of your linux servers

Requirements
* linux box
* Python 2.6 or higher
* [paramiko](http://www.lag.net/paramiko/) library
* Create/Commit rights to a CVS or Subversion repository
* cvs or svn binaries in the PATH

Installation:
-------------

To install, just do:

python setup.py install

Usage:
------

usage: ranlinconf.py [-h] [-c CONFIG] [--v] action

Track remotely configuration changes made to a list of linux servers between
successive runs.

positional arguments:
  action                Action to execute (RUN or GENCONFIG)

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file to use or create
  --v                   Print program version and exit.

Documentation:
--------------

Please visit the project page at: https://code.google.com/p/ranlinconf/

