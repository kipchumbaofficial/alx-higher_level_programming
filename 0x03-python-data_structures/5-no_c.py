#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        temp = my_string[:]
        for i in my_string:
            if i == 'c' or i == 'C':
                temp = my_string.translate({ord(i): None})
            my_string = temp
        return temp
