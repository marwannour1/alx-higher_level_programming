""" This module reads a file and prints its content to the console """


def read_file(filename=""):
    """ Read a file and print its content to the console """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
