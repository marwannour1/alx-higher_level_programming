#!/usr/bin/python3
"""Module to append a string after a specific string in a file"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string after a specific string in a file"""
    with open(filename, "r") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
    
    with open(filename, "w") as f:
        f.writelines(lines)
