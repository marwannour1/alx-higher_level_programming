#!/usr/bin/python3
"""Module to append a string after a specific string in a file"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string after a specific string in a file"""
    with open(filename, "r") as f:
        lines = f.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(new_lines)
