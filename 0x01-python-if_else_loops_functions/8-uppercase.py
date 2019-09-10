#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            st = ord(str[i]) - 32
        else:
            st = ord(str[i])
        print("{:c}".format(st), end='')
    print()
