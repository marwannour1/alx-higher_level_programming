#!/usr/bin/python3
""" This module saves an object to a file using JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ Save an object to a file using JSON representation """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
