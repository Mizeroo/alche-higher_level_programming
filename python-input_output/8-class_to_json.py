#!/usr/bin/python3
"""Module for converting a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Return the dict description of object for JSON serialization."""
    return obj.__dict__
