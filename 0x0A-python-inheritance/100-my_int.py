#!/usr/bin/python3
class MyInt(int):

    def __init__(self, num):
        self.num = num

    def __eq__(self, b):
        return not int.__eq__(self, b)

    def __ne__(self, b):
        return int.__eq__(self, b)
