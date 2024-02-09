#!/usr/bin/python3
""" This is a module that contains a function to check if an object is an
    instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """ This is a function that checks if an object is an instance of a class
        that inherited from the specified class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        True if the object is an instance of a class that inherited from the
        specified class, False otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
