#!/usr/bin/python3
"""This module contains the Rectangle class."""

from typing import Any
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

    # def __setattr__(self, name, value):
    #     """ This method sets the value of the attribute."""
    #     if name == "width":
    #         self.__width = value
    #     elif name == "height":
    #         self.__height = value
    #     elif name == "x":
    #         self.__x = value
    #     elif name == "y":
    #         self.__y = value

    # def __getattr__(self, name):
    #     """ This method gets the value of the attribute."""
    #     return self.__dict__[f"__{name}"]

    @property
    def width(self):
        """This method gets the value of the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets the value of the width attribute."""
        self.__width = value

    @property
    def height(self):
        """This method gets the value of the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets the value of the height attribute."""
        self.__height = value

    @property
    def x(self):
        """This method gets the value of the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """This method sets the value of the x attribute."""
        self.__x = value

    @property
    def y(self):
        """This method gets the value of the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """This method sets the value of the y attribute."""
        self.__y = value
