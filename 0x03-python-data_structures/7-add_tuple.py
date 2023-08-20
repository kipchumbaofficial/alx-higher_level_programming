#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = tuple_a + (0, 0)
    else:
        a = tuple_a
    if len(tuple_b) < 2:
        b = tuple_b + (0, 0)
    else:
        b = tuple_b
    return (a[0] + b[0], a[1] + b[1])
