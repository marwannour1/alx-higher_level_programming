#!/usr/bin/python3
def islower(c):
    if (ord(c) >= ord('a') and ord(c) <= ord('z')):
        return (True)
    return (False)


def uppsercase(str):
    for c in str:
        print("{:c}".format(ord(c) if islower(c) else ord(c) - 32),
            end='')
    print('')
