#!/usr/bin/python3
""" This module contains an empty class Rectangle that defines a rectangle."""


class Rectangle:
    """ Empty class Rectangle that defines a rectangle. """

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height
        Args:
            value (int): The height value to be set.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the current rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += "#" * self.__width
            if i != self.__height - 1:
                output += "\n"
        return output
 