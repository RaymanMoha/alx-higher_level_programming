#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary ordered by keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
