#!/usr/bin/python3
def number_of_lines(filename=""):
    n = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            n += 1
    return n
