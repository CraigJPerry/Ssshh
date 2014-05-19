#!/usr/bin/env python
# encoding: utf-8


"""Ssshh! SSH key management for application (i.e. non-human) user accounts."""

from setuptools import setup, find_packages


__version__ = "0.1.1"

README = open("README.rst").read()
REQUIREMENTS = open("requirements.txt").read()


setup(
    name="Ssshh",
    version=__version__,
    author="Craig J Perry",
    author_email="craigp84@gmail.com",
    description=__doc__,
    long_description=README,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

