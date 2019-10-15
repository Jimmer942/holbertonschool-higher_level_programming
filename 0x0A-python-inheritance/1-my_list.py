#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        cs = sorted(self)
        print(cs)
