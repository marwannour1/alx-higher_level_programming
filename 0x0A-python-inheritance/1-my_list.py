#!/usr/bin/python3
"""This is a module that contains a class MyList that inherits from list"""


class MyList(list):
    """This is a class MyList that inherits from list"""

    def print_sorted(self):
        """This is a method that prints the list, but sorted"""

        print(sorted(self)) 
