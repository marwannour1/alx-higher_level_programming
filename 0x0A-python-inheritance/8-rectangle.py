#!/usr/bin/python3
""" This module contains the class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ This method initializes the instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
