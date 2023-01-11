#!/usr/bin/python3
"""
This module provides write_file() function
"""


def write_file(filename="", text=""):
    """
    This is a functions that writes a string to a text file

    Args:
        param1 (filename): the file to be written
        param2 (text): the text to be written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

    return len(text)
