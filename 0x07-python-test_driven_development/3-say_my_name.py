#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
A module to print My name <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """
    python3 -c
    'print(__import__("my_module").my_function.__doc__)'
    Prints name in full
    """
    if first_name is None:
        raise TypeError("first_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
