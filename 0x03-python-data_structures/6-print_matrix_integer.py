#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for l in matrix:
        for i, n in enumerate(l):
            print("{:d}".format(n), end="")
            if i < len(l) - 1:
                print(" ",  end="")
        print()
