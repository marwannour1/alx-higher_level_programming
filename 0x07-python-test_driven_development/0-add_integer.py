#!/usr/bin/python3
""" This module adds two integers """


def add_integer(a, b=98):
    """ This function adds two integers
    Args:
        a: first integer will be casted to int if it is float
        b: second integer will be casted to int if it is float

    Returns:
        The sum of a and b

    Raises:
        TypeError: If a or b are not integers or floats
    """

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
