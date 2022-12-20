#!/usr/bin/python3
"""Sends a request to the specified URL, displays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
