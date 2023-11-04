#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
A module to print square in terms of '#'
"""


def print_square(size):
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for num in range(size):
            print("#", end="")
        print()
