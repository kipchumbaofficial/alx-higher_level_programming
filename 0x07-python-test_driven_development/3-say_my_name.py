#!/usr/bin/python3
'''
prints name
'''


def say_my_name(first_name, last_name=""):
    '''
    A function to print name
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
