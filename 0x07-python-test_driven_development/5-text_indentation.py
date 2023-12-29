#!/usr/bin/python3
'''
Text indentation
'''


def text_indentation(text):
    '''
    A funtion to indent text
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 1
    counter = 0
    for char in text:
        i += 1
        txt = text[counter:i - 1]
        if char in ['.', ':', '?']:
            print(txt, end="")
            print()
            counter = i
            print()
    print(txt)
