#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.0'

setup(
    name="django-html5-colorfield",
    version=version,
    keywords=["django", "color"],
    author='Tom Carrick',
    author_email='knyght@knyg.ht',
    url='https://github.com/knyghty/django-html5-colorfield',
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
