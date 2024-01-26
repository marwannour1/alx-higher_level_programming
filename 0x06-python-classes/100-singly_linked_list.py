#!usr/bin/python3
""" This module is responsible for creating a class
called Node which is used for a singly linked list

Author: Marwan Nourledin Mohamed Farag
Date: 26/1/2024
"""


class Node():
    """Node class with a private attribute called
    data and next_node and a constructor to initialize it.
    """

    def __init__(self, data, next_node=None):
        """ Constructor to initialize the private attribute
        data of the Node class to a given value or None by default

        Args:
            data (int): data of the node
            next_node (Node): next node of the current node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter method to retrieve the private attribute data

        Returns:
            The data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter method to set the private attribute data

        Args:
            value (int): data of the node

        Raises:
            TypeError: if data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter method to retrieve the private attribute next_node

        Returns:
            The next_node of the node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter method to set the private attribute next_node

        Args:
            value (Node): next node of the current node

        Raises:
            TypeError: if next_node is not a Node object
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """SinglyLinkedList class with a private attribute
    called head and a constructor to initialize it.
    """

    def __init__(self):
        """ Constructor to initialize the private attribute
        head of the SinglyLinkedList class to None
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Method to insert a new Node into the correct
        sorted position in the list (increasing order)

        Args:
            value (int): data of the node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node

        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """ Method to print the list in a specific format

        Returns:
            The list in the format [ <node data>, <node data>, ... ]
        """
        temp = self.__head
        output = ""
        while temp is not None:
            output += str(temp.data)
            if temp.next_node is not None:
                output += "\n"
            temp = temp.next_node
        return output
