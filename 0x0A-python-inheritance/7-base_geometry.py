#!/usr/bin/python3
"""This is a module that contains a class BaseGeometry"""


class BaseGeometry:
    """This is a class BaseGeometry"""
    def area(self):
        """This is a method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a method that validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
