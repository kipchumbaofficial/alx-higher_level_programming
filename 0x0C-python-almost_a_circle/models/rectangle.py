#!/usr/bin/python3
'''
Rectangle that inherits from base
'''

from models.base import Base


class Rectangle(Base):
    '''
    Rectangle definition
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns Area"""
        return self.__width * self.__height

    def display(self):
        """Prints rect with # character"""
        if self.__x != 0:
            for times in range(self.__y):
                print()
        for val in range(self.__height):
            if self.__x != 0:
                for numbers in range(self.__x):
                    print(" ", end="")
            for num in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Str customizTION"""
        retval = "[Rectangle] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        retval += "- {}/{}".format(self.__width, self.__height)
        return retval

    def update(self, *args):
        """Assigns an argument to each attribute"""

        argv = []

        for arg in args:
            argv.append(arg)

        if len(argv) > 0:
            self.id = argv[0]
        if len(argv) > 1:
            if not isinstance(argv[1], int):
                raise TypeError("width must be an integers")
            if argv[1] <= 0:
                raise ValueError("width must be > 0")
            self.__width = argv[1]
        if len(argv) > 2:
            if not isinstance(argv[2], int):
                raise TypeError("height must be an integer")
            if argv[2] <= 0:
                raise ValueError("height must be > 0")
            self.__height = argv[2]
        if len(argv) > 3:
            if not isinstance(argv[3], int):
                raise TypeError("x must be an integer")
            if argv[3] < 0:
                raise ValueError("x must be >= 0")
            self.__x = argv[3]
        if len(argv) > 4:
            if not isinstance(argv[4], int):
                raise TypeError("y must be an integer")
            if argv[4] < 0:
                raise ValueError("y must be >= 0")
            self.__y = argv[4]
