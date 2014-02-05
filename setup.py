#!/usr/bin/env python

from distutils.core import setup

version = '0.1.1'

setup(
    name="django-html5-colorfield",
    version=version,
    keywords=["django", "color"],
    author='Tom Carrick',
    author_email='knyght@knyg.ht',
    license='MIT',
    long_description="Provides an HTML5 color field for use in django models",
    description="Provides an HTML5 color django model field",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['colorfield'],
    install_requires=['django>=1.7'],
    requires=['django (>=1.7)'],
)
