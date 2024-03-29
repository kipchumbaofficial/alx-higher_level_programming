#!/usr/bin/python3

from sys import argv


def main():
    length = len(argv) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))

    for index in range(length):
        print("{}: {}".format(index + 1, argv[index + 1]))


if __name__ == "__main__":
    main()
