#!/usr/bin/python
# coding: utf8

import re
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("geocoder/__init__.py", "r") as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Cannot find version information")

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

requires = ["requests", "ratelim"]

setup(
    name="geocoder",
    version=version,
    description="Geocoder is a simple and consistent geocoding library.",
    long_description=readme,
    author="Denis Carriere",
    author_email="carriere.denis@gmail.com",
    url="https://github.com/jbylund/geocoder",
    download_url="https://github.com/jbylund/geocoder",
    license="The MIT License",
    entry_points="""
        [console_scripts]
        geocode=geocoder.cli:cli
    """,
    packages=["geocoder"],
    package_data={"": ["LICENSE", "README.md"]},
    package_dir={"geocoder": "geocoder"},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords="geocoder arcgis tomtom opencage google bing here",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: GIS",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
