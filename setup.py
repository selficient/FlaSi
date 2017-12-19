# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="FlaSi",
    author_email="mart.noten@student.hu.nl",
    url="",
    keywords=["Swagger", "FlaSi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    The FlaSi webservice connects the HomeLynk system to the outside world. It is the main entry point into the Selficient house. It gives the user the possibility to read the MySQL database that is connected to the house, as well as send signals to the local domotica objects
    """
)

