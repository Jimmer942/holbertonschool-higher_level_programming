#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        c = i - 32
    else:
        c = i
    print("{:c}".format(c), end='')
