#!/usr/bin/python3

'''
Print lowercase to upper
'''


def uppercase(str):
    '''Function printing lowercase to uppercase
    '''
    for char in str:
        if ord(char) in range(97, 123):
            new_asci = ord(char) - 32
        else:
            new_asci = ord(char)
        print(chr(new_asci), end="")
    print()
