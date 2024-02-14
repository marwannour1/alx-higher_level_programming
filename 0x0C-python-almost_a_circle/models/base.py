#!/usr/bin/python3
"""This module contains the base class for all models in the application."""


class Base:
    """This class is the base class for all models in the application."""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
