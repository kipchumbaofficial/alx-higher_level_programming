#!/usr/bin/python3

import hidden_4


def main():
    for arg in dir(hidden_4):
        if arg[0] == '_':
            continue
        print(arg)


if __name__ == "__main__":
    main()
