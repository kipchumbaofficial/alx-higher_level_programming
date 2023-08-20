#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for i, n in enumerate(row):
            print("{:d}".format(n), end="")
            if i < len(row) - 1:
                print(" ",  end="")
        print()
