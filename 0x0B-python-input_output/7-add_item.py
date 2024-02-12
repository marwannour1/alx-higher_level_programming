#!/usr/bin/python3
""" This module adds all arguments to a Python list, and then saves them to a
file """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file




arglist = list(sys.argv[1:])

try:
    my_list = load_from_json_file("add_item.json")

except Exception as e:
    my_list = []

my_list.extend(arglist)
save_to_json_file(my_list, "add_item.json")