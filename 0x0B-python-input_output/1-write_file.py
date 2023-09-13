#!/usr/bin/python3
"""
Writes to a txt file in utf-8
"""


def write_file(filename="", text=""):
    """
    writes to a file and returns characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
