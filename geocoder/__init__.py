#!/usr/bin/python
# coding: utf8


"""
Geocoder
~~~~~~~~

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

"""

__title__ = "geocoder"
__author__ = "Denis Carriere"
__author_email__ = "carriere.denis@gmail.com"
__version__ = "1.38.1"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2013-2016 Denis Carriere"

# EXTRAS
# CORE
from geocoder.api import gisgraphy  # noqa
from geocoder.api import (
    arcgis,
    baidu,
    bing,
    canadapost,
    distance,  # noqa
    elevation,
    freegeoip,
    gaode,
    geocodefarm,
    geolytica,
    geonames,
    get,
    google,
    here,
    ip,
    ipinfo,
    komoot,
    location,
    locationiq,
    mapbox,
    mapquest,
    mapzen,
    maxmind,
    nokia,
    opencage,
    osm,
    ottawa,
    places,
    reverse,
    tamu,
    tgos,
    timezone,
    tomtom,
    uscensus,
    w3w,
    yahoo,
    yandex,
)

# CLI
from geocoder.cli import cli  # noqa
