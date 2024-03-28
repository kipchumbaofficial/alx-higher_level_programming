#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            new_asci = ord(char) - 32
        else:
            new_asci = ord(char)
        print("{}".format(chr(new_asci)), end="")
    print()
