#!/usr/bin/python3
""" This module returns an object represented by a JSON string from a file """


import json


def load_from_json_file(filename):
    """ Return an object represented by a JSON string from a file """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
