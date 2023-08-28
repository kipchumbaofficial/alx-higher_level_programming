#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    elements = 0
    try:
        for value in my_list:
            i += 1
            if i <= x:
                print("{}".format(value), end="")
                elements += 1
        print()
    except Exception as error:
        print(error);
    return elements
