#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='strf',
    version='0.0.1',
    description="string format locals",
    author="Douglas La Rocca",
    author_email='larocca@larocca.io',
    url='https://github.com/douglas-larocca/strf',
    license="BSD",
    zip_safe=False,
    keywords='string format locals inspect',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)