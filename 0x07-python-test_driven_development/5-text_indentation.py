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
            while i < len(text) and text[i].isspace():
                i += 1
            print(txt, end="")
            print()
            counter = i
            print()
    if counter == 0:
        print(text[counter:])
    else:
        print(text[counter - 1:])
