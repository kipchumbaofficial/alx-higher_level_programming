#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, elements = 0, 0
    try:
        for value in my_list:
            i += 1
            if i <= x:
                if isinstance(value, int):
                    print("{:d}".format(value), end="")
                    elements += 1
        print()
    except Exception:
        print("Error!")
    return elements
