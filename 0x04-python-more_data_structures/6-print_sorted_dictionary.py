#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.items())
    for i, j in a:
        print("{}: {}".format(i, j))
