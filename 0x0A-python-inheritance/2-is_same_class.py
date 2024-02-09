#!/usr/bin/python3
""" This is module that contains a function to check if an object is an
    instance of a class
"""


def is_same_class(obj, a_class):
    """ This is a function that checks if an object is an instance of a class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        True if the object is an instance of the class, False otherwise
    """

    return type(obj) == a_class
