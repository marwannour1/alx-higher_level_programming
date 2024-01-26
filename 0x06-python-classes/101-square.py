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

    def __init__(self, size=0, position=(0, 0)):
        """ Constructor to initialize the private attribute
        size of the Square class to a given value or 0 by default

        Args:
            size (int): size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter method to retrieve the private attribute position

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method to set the private attribute position

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or not
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """" Method to calculate the area of the square

        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method to print the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """ Method to print the square with the character #
        """
        self.my_print()
        return ""
