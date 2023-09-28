#!/usr/bin/python3
'''
A class with delete message
'''


class Rectangle:
    '''
    Setting delete message
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        retval = ""

        if self.__width != 0 and self.__height != 0:
            for indx in range(self.__height):
                retval += str(self.print_symbol) * self.__width
                if indx + 1 < self.__height:
                    retval += "\n"
        return retval

    def __repr__(self):
        retrep = "Rectangle(" + str(self.__width) + ", "
        retrep += str(self.height) + ")"
        return retrep

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1
