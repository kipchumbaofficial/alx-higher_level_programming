#!/usr/bin/python3
"""6-main"""

max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
print(max_integer())
print(max_integer(None))
print(max_integer([10]))
