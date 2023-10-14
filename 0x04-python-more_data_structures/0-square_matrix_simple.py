#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        temp = []
        for item in row:
            temp.append(item ** 2)
        new_matrix.append(temp)
    return (new_matrix)
