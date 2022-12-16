#!/bin/bash
#sends a JSON POST request to the specified URL and displays the body of the response.
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
