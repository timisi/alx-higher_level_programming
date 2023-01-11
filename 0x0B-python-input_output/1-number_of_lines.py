#!/usr/bin/python3
"""
This module provides number_of_lines() function
"""


def number_of_lines(filename=""):
    """
    This is a function that return de number of lines of a text file

    Args:
        param1 (filename): the file to be read and check
    """
    line = 0
    with open(filename, encoding="utf-8") as f:
        for i in f:
            line += 1

    return line
