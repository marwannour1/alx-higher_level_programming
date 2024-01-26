#!/usr/bin/python3
"""
This module is responsible for creating a class called Square

Author: Marwan Nourledin Mohamed Farag
Date: 26/1/2024
"""


class Square():
    """
    Square class with a private attribute called size and
    a constructor to initialize it.
    """

    def __init__(self, size=0):
        """ Constructor to initialize the private attribute
        size of the Square class to a given value or 0 by default
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
