#!/usr/bin/python3
""" This module contains an empty class Rectangle that defines a rectangle."""


class Rectangle:
    """ Empty class Rectangle that defines a rectangle. """

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle data"""
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieves the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value
