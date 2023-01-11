#!/usr/bin/python3
"""
This module provides read_lines() function
"""


def read_lines(filename="", nb_lines=0):
    """
    This is a function that reads n lines of a text file

    Args:
        param1 (filename): the file to be readed and printed
        param2 (nb_lines): number of lines to be readed
    """
    with open(filename, encoding="utf-8") as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
