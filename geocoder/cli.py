#!/usr/bin/python
# coding: utf8
import argparse
import fileinput
import json
import os

from .api import options

providers = sorted(options)
methods = ["geocode", "reverse", "elevation", "timezone", "places"]
outputs = ["json", "osm", "geojson", "wkt"]
units = ["kilometers", "miles", "feet", "meters"]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("location")
    parser.add_argument("--provider", "-p", default="osm", choices=providers)
    parser.add_argument("--method", "-m", default="geocode", choices=methods)
    parser.add_argument("--output", "-o", default="json", choices=outputs)
    parser.add_argument("--units", "-u", default="kilometers", choices=units)
    parser.add_argument("--timeout", "-t", default=5.0)
    parser.add_argument("--distance", is_flag=True)
    parser.add_argument("--language", default="")
    parser.add_argument("--url", default="")
    parser.add_argument("--proxies")
    parser.add_argument("--key")
    # following are for Tamu provider
    parser.add_argument("--city", "-c", default="")
    parser.add_argument("--state", "-s", default="")
    parser.add_argument("--zipcode", "-z", default="")
    return vars(parser.parse_args())


def cli():
    """Geocode an arbitrary number of strings from Command Line."""

    locations = []

    # Read Standard Input
    # $ cat foo.txt | geocode
    try:
        for line in fileinput.input():
            locations.append(line.strip())
    except:
        pass

    # Read multiple files & user input location
    for item in location:
        if os.path.exists(item):
            with open(item, "rb") as f:
                locations += f.read().splitlines()
        else:
            locations.append(item)

    # Distance calculation
    if kwargs["distance"]:
        d = geocoder.distance(locations, **kwargs)
        print(d)
        return

    # Geocode results from user input
    for location in locations:
        g = geocoder.get(location.strip(), **kwargs)
        try:
            print(json.dumps(getattr(g, kwargs["output"])))
        except IOError:
            # When invalid command is entered a broken pipe error occurs
            return


if __name__ == "__main__":
    cli()
