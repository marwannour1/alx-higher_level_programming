#!/usr/bin/python3
""" This module will sole N-queens problem. """


import sys

class Board():
    """ Class that represents a board. """
    def __init__(self, n):
        """ Initialize the board. """
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.solutions = []

    @property
    def n(self):
        """ Retrieve the value of n. """
        return self.__n

    @n.setter
    def n(self, value):
        """ Set the value of n. """
        if type(value) is not int:
            print("n must be a number")
            exit(1)
        if value < 4:
            print("n must be at least 4")
            exit(1)

        self.__n = value    

    def print_board(self):
            """ Print the board.

            This method prints the current state of the chess board.
            Each row is printed on a separate line, with each cell represented by a symbol.
            """
            for row in self.board:
                print(row)

    def is_safe(self, row, col):
        """ Check if a queen can be placed on board[row][col]. """
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def solve(self, col):
        """ Solve the N-queens problem. """
        if col == self.n:
            self.solutions.append(self.board)
            return True
        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve(col + 1) or res
                self.board[i][col] = 0
        return res
