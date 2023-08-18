#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_int = 0
    previous = 0
    if roman_string is None:
        return my_int
    for i in roman_string:
        if i in my_dict:
            current = my_dict[i]
            if current > previous:
                my_int += current - 2 * previous
            else:
                my_int += current
            previous = current
    return my_int
