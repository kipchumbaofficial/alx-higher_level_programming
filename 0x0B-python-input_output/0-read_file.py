#!/usr/bin/python3
"""
Reads and print a file
"""
def read_file(filename=""):
    """Reads and prints a
    file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
