#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import kvisits

setup(
    name = 'django-kvisits',
    version = ":versiontools:kvisits:",
    description = "Visit counter for model objects and urls",
    long_description = "",
    keywords = 'django, visit, counter',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/kaleidos/django-kvisits',
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
