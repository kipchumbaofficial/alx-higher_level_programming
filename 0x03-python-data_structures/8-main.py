#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

length, first = multiple_returns("At school, I learned C!")
print("length: {:d} - first character: {}".format(length, first))
