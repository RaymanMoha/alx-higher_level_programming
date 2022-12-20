#!/usr/bin/python3
"""Sends a request to the specified URL and displays the value of the
variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
