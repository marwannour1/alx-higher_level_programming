#!/usr/bin/python3
"""This module contains the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """This is the class for Rectangle objects."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a new instance of the Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This method gets the value of the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the value of the width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This method gets the value of the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the value of the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This method gets the value of the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """This method sets the value of the x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This method gets the value of the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """This method sets the value of the y attribute."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of the Rectangle object."""
        return self.width * self.height
