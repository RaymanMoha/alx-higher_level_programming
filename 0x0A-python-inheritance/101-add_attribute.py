#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.
    Args:
        obj (any): object to add an attribute
        att (str): name of the attr to add to obj
        value (any): value of the attribute
    Raises:
        TypeError: if the attr can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
