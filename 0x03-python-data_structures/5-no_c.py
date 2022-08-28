#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters c and C from a string."""
    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new_string))
