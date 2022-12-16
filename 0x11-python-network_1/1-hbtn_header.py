#!/usr/bin/python3
"""Sends a request to the specified URL and displays
the value of the X-Request-Id in the header of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
