#!/bin/bash
# Script that sends a GET request with a custom header and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
