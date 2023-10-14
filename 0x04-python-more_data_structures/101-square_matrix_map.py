#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
