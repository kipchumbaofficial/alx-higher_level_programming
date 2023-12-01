#!/usr/bin/python3
'''
Prints a square
'''


def print_square(size):
    '''
    A function to print a square
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for l in range(size):
        for i in range(size):
            print("#", end="")
        print()
