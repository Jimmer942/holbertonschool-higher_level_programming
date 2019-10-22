#!/usr/bin/python3
from models.base import Base
""" Module class Base """


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes properties"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """ x getter """
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area """
        return self.width * self.height

    def display(self):
        """ Display """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(self.y):
                print()
            reg = ""
            for i in range(self.height):
                for i in range(self.x):
                    print(" ", end='')
                for j in range(self.width):
                    reg += "#"
                    print("#", end='')
                reg += "\n"
                print()
        return reg[:-1]

    def __str__(self):
        """ Print """
        s1 = "[Rectangle] ({}) {}/{} - ".format(self.id, self.x, self.y)
        s2 = "{}/{}".format(self.width, self.height)
        return s1 + s2

    def update(self, *args, **kwargs):
        """ Update """
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
