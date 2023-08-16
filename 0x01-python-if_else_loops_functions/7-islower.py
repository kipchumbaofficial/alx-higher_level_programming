#!/usr/bin/python3
def islower(c):
    for value in range(97, 123):
        if ord(c) == value:
            return True
    return False
