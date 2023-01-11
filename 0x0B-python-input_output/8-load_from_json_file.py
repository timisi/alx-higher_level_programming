#!/usr/bin/python3
"""
This module provides load_from_json_file() function
"""
import json


def load_from_json_file(filename):
    """
    This is a function that creates an object from a JSON file

    Args:
        param1 (filename): file that gives the information of the new object
    """
    with open(filename, encoding="utf-8") as f:
        pars = f.read()

    return json.loads(pars)
