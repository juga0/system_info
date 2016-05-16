#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)


def obtain_python_version():
    import sys
    python_version = sys.version
    logger.debug('python version %s' % python_version)
    return python_version


def obtain_uname():
    from os import uname
    kernel_version = ' '.join(uname())
    logger.debug('kernel version %s' % kernel_version)
    return kernel_version


def obtain_system_hostname():
    import socket
    host = socket.gethostname()
    logger.debug('host %s' % host)
    return host


def obtain_user():
    import getpass
    user = getpass.getuser()
    logger.debug('user %s' % user)
    return user


def obtain_home():
    # from os.path import expanduser
    # home = expanduser('~')
    from os import environ
    home = environ['HOME']
    logger.debug('home %s' % home)
    return home


def obtain_environ():
    from os import environ
    logger.debug('environ %s' % environ)
    return environ

def main():
    obtain_python_version()
    obtain_uname()
    obtain_system_hostname()
    obtain_user()
    obtain_home()
    obtain_environ()


if __name__ == "__main__":
    main()
