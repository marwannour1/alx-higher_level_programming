#!/usr/bin/python3
"""This module prints a square with the character #"""


def print_square(size):
    """This function prints a square with the character #
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end='\n' if i != size - 1 else '')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
