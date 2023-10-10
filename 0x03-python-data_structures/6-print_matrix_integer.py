#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for row in matrix:
        if len(row) == 0:
            print()
        for col in range(0, len(row)):
            print("{:d}".format(row[col]), end='\n'
                  if col == (len(row) - 1) else ' ')
