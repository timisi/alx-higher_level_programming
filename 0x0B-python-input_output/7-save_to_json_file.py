#!/usr/bin/python3
"""
This module provides save_to_json_file() function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This is a functions that writes an object to a text file

    Args:
        param1 (my_obj): object to be written in a file
        param2 (filename): file to be written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
