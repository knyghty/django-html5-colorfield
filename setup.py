#!/usr/bin/env python

from distutils.core import setup

version = '0.1.1'

setup(
    name="django-html-colorfield",
    version=version,
    keywords=["django", "color"],
    author='Tom Carrick',
    author_email='knyght@knyg.ht',
    license='MIT',
    long_description="A small app providing a colorpicker field for django",
    description="A small app providing a colorpicker field for django",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['colorfield'],
    install_requires=['django>=1.7'],
    requires=['django (>=1.7)'],
)
