#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for i in range(len(matrix)):
        squares.append(list(map(lambda x: x ** 2, matrix[i])))
    return squares
