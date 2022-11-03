<<<<<<< HEAD
#!/bin/python3

import json

def from_json_string(my_str):
    """a function that returns json rep on object"""
    return json.dumps(my_str)

=======
#!/usr/bin/python3
"""Module 3-to_json_string.
Returns the JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """Returns th JSON representation of my_obj.
    Args:
        - my_obj: string to represent
    Returns: JSON representation
    """

    return json.dumps(my_obj)
>>>>>>> fa5821ef6204bdc139f8085292c2107a63c7445c
