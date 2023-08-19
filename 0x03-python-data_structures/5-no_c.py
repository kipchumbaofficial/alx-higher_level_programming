#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        for i in my_string:
            if i == 'c' or i == 'C':
                return my_string.translate({ord(i): None})
