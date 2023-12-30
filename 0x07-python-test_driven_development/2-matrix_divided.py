#!/usr/bin/python3
'''
python3 -c 'print(__import__("my_module").__doc__)
A module to divide elemets of a matrix
'''


def matrix_divided(matrix, div):
    """A function to divid a matrxi by div
    """

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
    row_sizes = [len(row) for row in matrix]
    equal_sizes = [i + 1 for i, size in enumerate(row_sizes)
                   if size == row_sizes[0]]
    if len(equal_sizes) != len(row_sizes):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []

    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        result.append(new_row)
    return result
