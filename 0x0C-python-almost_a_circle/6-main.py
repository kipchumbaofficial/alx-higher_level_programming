#!/usr/bin/python3

from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(10, 12, 0, 1)
    r2.display()
