#!/usr/bin/python3
""" This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix
    Args:
        matrix: list of lists of integers or floats
        div: integer or float
    Returns: new matrix
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If matrix contains rows of different sizes
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is zero
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not all(isinstance(row, list) and len(row) != 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not all(isinstance(element, (int, float)) for
               row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must\
 have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
