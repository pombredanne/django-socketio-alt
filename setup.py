#!/usr/bin/env python
import os

from setuptools import setup


def long_description():
    path = os.path.dirname(__file__)
    path = os.path.join(path, 'README.rst')
    try:
        with open(path) as f:
            return f.read()
    except:
        return ''


__doc__ = long_description()


setup(
    name='django-socketio-alt',
    version='0.2',
    url='https://github.com/amirouche/django-socketio-alt',
    license='LGPL',
    author='Amirouche Boubekki',
    author_email='amirouche.boubekki@gmail.com',
    description='Django + Gevent + SocketIO = Awesome client/server interactions',
    long_description=__doc__,
    py_modules=['djsocketio'],
    zip_safe=False,
    platforms='any',
    install_requires=['django==1.4.2', 'gevent-socketio'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
)
