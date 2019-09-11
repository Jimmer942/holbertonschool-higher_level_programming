#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return (str)
    aux = ""
    for i in range(len(str)):
        if i == n:
            aux = aux + ""
        else:
            aux = aux + str[i]
    return (aux)
