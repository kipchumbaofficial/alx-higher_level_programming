#!/usr/bin/python3

"""
Creates and write to if it doesnt exist
Overwrites if it exits
"""

def write_file(filename="", text=""):
    """Writes to a file"""

    with open(filename, "w+", encoding="utf-8") as f:
        retval = f.write(text)
    return retval
