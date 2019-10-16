#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="utf-8") as f:
        if (nb_lines > 0):
            line = f.readline()
            n = 0
            while n != nb_lines:
                print(line, end='')
                line = f.readline()
                n += 1
        else:
            read_data = f.read()
            print(read_data, end='')
