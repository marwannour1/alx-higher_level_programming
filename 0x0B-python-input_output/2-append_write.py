#!/usr/bin/python3
""" This module appends a string to a text file """


def append_write(filename="", text=""):
    """ Write a string to a text file """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
