#!/bin/bash
set -e


echo "Local Smoke Test"
STD_APP_URL=http://localhost:8000
echo

# Test: Get the list of user websites
echo "=== Get the list of user websites ==="
ENDPOINT=/api/users/websites
echo ${STD_APP_URL}${ENDPOINT}
curl -s -XGET  "${STD_APP_URL}${ENDPOINT}" | jq .
echo

# Test: Get list of users details ordered
echo "=== Get list of users details ordered ==="
ENDPOINT=/api/users/detail
echo ${STD_APP_URL}${ENDPOINT}
curl -s -XGET  "${STD_APP_URL}${ENDPOINT}" | jq .
echo
