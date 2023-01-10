#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ function reads n lines of a text file (UTF8) prints it stdout """

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            [print(i, end='') for i in lines]
        else:
            [print(lines[i], end='') for i in range(0, nb_lines)]
