#!/bin/bash
# Script that sends a GET request to a URL and displays the body of a 200 response
curl -s "$1" -w "%{http_code}" | grep -v "^[^2]"
