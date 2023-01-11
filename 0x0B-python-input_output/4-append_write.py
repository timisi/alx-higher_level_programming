#!/usr/bin/python3
"""
This module provides append_write() function
"""


def append_write(filename="", text=""):
    """
    This is a function that appends a string at the end of the file

    Args:
        param1 (filename): the file to be appended
        param2 (text): the text to be appended
    """
    with open(filename, mode='a+', encoding="utf-8") as f:
        f.write(text)

    return len(text)
