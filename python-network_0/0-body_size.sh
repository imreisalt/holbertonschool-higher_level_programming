#!/bin/bash
# Script that sends a request to a URL and displays the size of the body response in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
