#!/usr/bin/python3
"""
Append to a file
Creates if a file doesn't exist
"""


def append_write(filename="", text=""):
    """Appends a file"""

    with open(filename, 'a+', encoding="utf-8") as f:
        retval = f.write(text)
    return retval
