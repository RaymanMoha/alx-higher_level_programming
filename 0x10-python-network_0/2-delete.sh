#!/bin/bash
# Sends a DELETE request to the specified URL and displays the body of the response.
curl -s "$1" -X DELETE
