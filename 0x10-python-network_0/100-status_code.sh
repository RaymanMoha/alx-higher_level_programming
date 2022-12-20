#!/bin/bash
# sends a request to the specified URL and displays the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
