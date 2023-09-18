#!/usr/bin/python3
'''
A square class
'''


class Square:
    '''
    class with size value and type exeptions
    '''
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
