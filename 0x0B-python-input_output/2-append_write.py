#!/usr/bin/python3
"""
Appensds a file
"""


def append_write(filename="", text=""):
    """
    Appends and return number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
