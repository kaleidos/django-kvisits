#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import modelsubscription

setup(
    name = 'django-modelsubscription',
    version = ":versiontools:modelsubscription:",
    description = "Generic model mixin for user or email subscription to objects",
    long_description = "",
    keywords = 'django, model',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/kaleidos/django-modelsubscription',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
