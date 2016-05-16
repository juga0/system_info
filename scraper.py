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


def obtain_dir():
    from os import listdir
    ls = listdir('/app')
    logger.debug('ls /app %s' % ls)
    return obtain_dir


def obtain_ip():
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    ip2 = socket.gethostbyname_ex(socket.gethostname())
    logger.debug('ip %s' % ip)
    # logger.debug('ip2 %s' % ip2)
    return ip


def obtain_public_ip():
    from urllib2 import urlopen
    from json import load
    try:
        my_ip = urlopen('http://ip.42.pl/raw').read()
    except:
        try:
            my_ip = load(urlopen('http://jsonip.com'))['ip']
        except:
            try:
                my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
            except:
                try:
                    my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
                except:
                    my_ip = None
    logger.debug('public ip %s' % my_ip)
    return my_ip


def main():
    obtain_python_version()
    obtain_uname()
    obtain_system_hostname()
    obtain_user()
    obtain_home()
    obtain_environ()
    obtain_dir()
    obtain_ip()
    obtain_public_ip()


if __name__ == "__main__":
    main()
