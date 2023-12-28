#!/usr/bin/python3
'''
pytho3 -c 'print(__import__("my_module").__doc__)'
Reads a file
'''


def read_file(filename=""):
    '''
    Reads file
    '''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
