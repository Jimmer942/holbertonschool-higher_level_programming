#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            c += 1
            print(my_list[i], end='')
        except:
            c -= 1
            break
    print()
    return c
