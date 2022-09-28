#!/usr/bin/python3
""" Module that contains  returns the JSON representation of an object (string):
"""
import json
def to_json_string(my_obj):
   """Args:
          my_obj: object
    Raises:
           Exception: when the string can't be decoded"""
		
return json.dumps(my_obj)
