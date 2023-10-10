#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            print("{:d}".format(matrix[row][col], end='\n' if col == (len(matrix[row]) - 1) else ' '))
