#!/usr/bin/python3
"""Takes in a URL and email address, sends a POST request to the URL with
the email as a parameter, and displays the body of the response"""


if __name__ == "__main__":
    import sys
    import requests

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
