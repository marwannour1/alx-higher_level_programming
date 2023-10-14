#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = {item for item in set_1 if item not in set_2}
    d_set = {item for item  in set_2 if item not in set_1}
    return (c_set + d_set)
