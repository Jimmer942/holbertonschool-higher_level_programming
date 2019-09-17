#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]
    if (a == 0):
        new_tuple = (0, None)
    else:
        new_tuple = (a, b)
    return new_tuple
