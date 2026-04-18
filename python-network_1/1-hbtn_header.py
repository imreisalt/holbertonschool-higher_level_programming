#!/usr/bin/python3
"""Script that fetches a URL and displays the X-Request-Id header value"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
