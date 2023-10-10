#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (None)
    res = []
    for num in my_list:
        res.append(num % 2 == 0)
    return res
