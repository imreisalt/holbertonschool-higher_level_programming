#!/bin/bash
# Script that displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -v 2>&1 | grep "Allow"
