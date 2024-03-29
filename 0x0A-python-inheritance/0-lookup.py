#!/usr/bin/python3
""" Module that contains a function that returns a list of available attributes
    and methods of an object
"""


def lookup(obj):
    """ Function that returns a list of available attributes and methods of an
        object
    """
    return dir(obj)
