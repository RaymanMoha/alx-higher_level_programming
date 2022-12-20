#!/usr/bin/python3
"""Takes in a URL and email, sends a POST request to the URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
