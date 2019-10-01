#!/usr/bin/python3
class Square:
        _size = 0

        def __init__(self, new_size=0):
            if type(new_size) is not int:
                raise TypeError('size must be an integer')
            if new_size < 0:
                raise ValueError('size must be >= 0')
            self._Square__size = new_size

        def area(self):
            return self._Square__size ** 2

        @property
        def size(self):
            return self._Square__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError('size must be >= 0')
            self._Square__size = value

        def my_print(self):
                if(self._Square__size == 0):
                        print()
                else:
                        for i in range(self._Square__size):
                                for j in range(self._Square__size):
                                        print("#", end='')
                                print()
