#!/usr/bin/python
# coding: utf8

import geocoder

location = "99.240.181.199"


def test_freegeoip():
    g = geocoder.freegeoip(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    print(g.debug())
    assert osm_count >= 2
    assert fields_count >= 10
