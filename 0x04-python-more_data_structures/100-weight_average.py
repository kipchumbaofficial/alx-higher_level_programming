#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sum_num += (my_list[i][0] * my_list[i][1])
        sum_den += mylist[i][1]
    return sum_num / sum_den
