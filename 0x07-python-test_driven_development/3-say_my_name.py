#!/usr/bin/python3
"""This module prints a name and a last name"""

def say_my_name(first_name, last_name=""):
    """This function prints a name and a last name
    Args:
        first_name (str): First name
        last_name (str): Last name
    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
