#!/usr/bin/python3
""" This module contains the Square class. """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the class for Square objects. """

    def __init__(self, size, x=0, y=0, id=None):
        """ This method initializes a new instance of the Square class. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This method returns a string representation of the Square object. """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
