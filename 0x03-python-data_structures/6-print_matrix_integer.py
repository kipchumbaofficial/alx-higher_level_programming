#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for l in matrix:
        for i in l:
            print("{:d}".format(i), end=" ")
        print()
