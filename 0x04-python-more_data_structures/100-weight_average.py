#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    sum_num = 0
    sum_den = 0
    if len(my_list) == 0:
        return 0
    for t in my_list:
        sum_num += (t[0] * t[1])
        sum_den += t[1]
    return sum_num / sum_den
