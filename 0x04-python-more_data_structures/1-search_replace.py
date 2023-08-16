#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = my_list[:]
    for i, value in enumerate(my_list):
        if value == search:
            temp[i] = replace

    return temp
