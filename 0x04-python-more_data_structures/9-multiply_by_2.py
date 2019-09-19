#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for i, j in a.items():
        a[i] = j * 2
    return a
