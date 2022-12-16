#!/bin/bash
# Sends a GET request to the specified URL, and displays the body of the response.
curl -sfL "$1" -X GET
