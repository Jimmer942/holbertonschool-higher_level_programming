#!/usr/bin/env python3

""" Find peak """


def find_peak(list_of_integers):
    """ Find peak """
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for i in list_of_integers:
        if i > peak:
            peak = i
    return peak
