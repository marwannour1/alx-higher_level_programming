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

    def update(self, *args, **kwargs):
        """ This method updates the attributes of the Square object. """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ This method returns the dictionary representation of a Square
        object. """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
