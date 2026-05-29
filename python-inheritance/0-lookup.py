#!/usr/bin/python3
"""Module that provides a function to look up an object's attributes and methods."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)