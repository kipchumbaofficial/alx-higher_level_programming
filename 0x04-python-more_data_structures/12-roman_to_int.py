#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_int = 0
    if roman_string == None:
        return my int
    for i in roman_string:
        for key, value in my_dict.items():
            if key == i:
                my_int += value
    return my_int
