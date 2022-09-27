#!/usr/bin/python3
"""Defines a text-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the no. of characters"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)
