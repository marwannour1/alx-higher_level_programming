#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index, count = 0, 0
    try:
        while index < x:
            if type(my_list[index]) == type(4):
                print(my_list[index], end='')
                count += 1
            index += 1
    except IndexError:
        None
    print()
    return (count)
