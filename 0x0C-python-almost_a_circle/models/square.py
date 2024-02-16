#!/usr/bin/python3
""" This module contains the Square class. """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the class for Square objects. """

    def __init__(self, size, x=0, y=0, id=None):
        """ This method initializes a new instance of the Square class. """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This method returns a string representation of the Square
        object. """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ This method gets the value of the size attribute. """
        return self.width

    @size.setter
    def size(self, value):
        """ This method sets the value of the size attribute. """
        self.width = value
        self.height = value
