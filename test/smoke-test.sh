#!/bin/bash
set -e

echo "Local Smoke Test"
STD_APP_URL=http://localhost:8000

echo STD_APP_URL=${STD_APP_URL}

# Test: Get the list of user websites
echo "=== Get the list of user websites ==="
curl -s -XGET  "${STD_APP_URL}/api/users/websites" | jq .
