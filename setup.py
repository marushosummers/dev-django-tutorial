# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

# See Pipfile for checking dependencies
setup(
    name='python-prototypes',
    version='0.1.0',
    description='Python Prototypes',
    long_description=readme,
    url='https://github.com/estie-inc/python-prototypes',
    packages=find_packages(exclude=('tests', 'docs'))
)
