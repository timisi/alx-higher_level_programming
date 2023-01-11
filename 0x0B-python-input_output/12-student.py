#!/usr/bin/python3
"""
This module provides Student class
"""


class Student:
    """
    Class of Student

    Attributes:
        attr1 (first_name): first name of the student
        attr2 (last_name): last name of the student
        attr3 (age): age of the student
    """
    def __init__(self, first_name, last_name, age):
        """
        This is the constructor of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        items = {}
        if type(attrs) is list:
            for attribute, value in self.__dict__.items():
                if attribute in attrs:
                    items[attribute] = value
        else:
            for attribute, value in sorted(self.__dict__.items()):
                items[attribute] = value

        return items
