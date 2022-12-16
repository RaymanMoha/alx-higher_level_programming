#!/usr/bin/python3
"""Sends a request to the specified URL and displays the body of the
response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
