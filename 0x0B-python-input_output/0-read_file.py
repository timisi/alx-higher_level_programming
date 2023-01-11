#!/usr/bin/python3
"""
This module provides read_file() function
"""


def read_file(filename=""):
    """
    This is a function that reads a text file and prints it

    Args:
        param1 (filename): the file to be read and print
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
