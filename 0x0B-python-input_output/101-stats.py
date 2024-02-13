#!/usr/bin/python3
""" Module to write a script that reads stdin line by line and computes metrics
:"""


from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
counter = 0


def printer():
    """Prints the accumulated metrics"""
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


try:
    for line in stdin:
        data = line.split()
        if len(data) >= 2:
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            total_size += int(data[-1])

        counter += 1

        if counter % 10 == 0:
            printer()
    printer()

except KeyboardInterrupt as e:
    printer()
