#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open('README.md') as readme_file:
    readme = readme_file.read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='strf',
    packages=['strf'],
    version='0.0.2',
    description="string format locals",
    long_description=readme,
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
