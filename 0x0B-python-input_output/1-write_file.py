#!/usr/bin/python3
""" This module writes a string to a text file """


def write_file(filename="", text=""):
    """ Write a string to a text file """

    with open (filename, 'w', encoding='utf-8') as file:
        return file.write(text)
