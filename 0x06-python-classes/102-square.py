#!/usr/bin/python3
"""
This module is responsible for creating a class called Square

Author: Marwan Nourledin Mohamed Farag
Date: 26/1/2024
"""


class Square():
    """Square class with a private attribute called size and
    a constructor to initialize it.
    """

    def __init__(self, size=0):
        """ Constructor to initialize the private attribute
        size of the Square class to a given value or 0 by default

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Getter method to retrieve the private attribute size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set the private attribute size

        Args:
            value (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """" Method to calculate the area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if both objects are equal, False otherwise
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if both objects are not equal, False otherwise
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if self is less than other, False otherwise
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if self is less than or equal to other, False otherwise
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if self is greater than other, False otherwise
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """ Method to compare two Square objects

        Args:
            other (Square): another Square object

        Returns:
            True if self is greater than or equal to other, False otherwise
        """
        return (self.area() >= other.area())
