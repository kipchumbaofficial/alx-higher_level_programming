#!/usr/bin/python3
'''
pytho3 -c 'print(__import__("my_module").__doc__)'
Reads a file
'''


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
