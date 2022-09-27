#!/usr/bin/python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout."""
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
