#!/bin/bash
set -e


#!/bin/bash

# Check developer env has pip libraries or conda dependencies.
# If error out here, re-create your environment via conda env update -f environment_dev.yml
PIP_LIST_FILE=$(mktemp)
conda list | awk 'NR>3 {print $1}' > ${PIP_LIST_FILE}
DEPENDENCIES_LIST=$(cat environment_dev.yml | awk 'NR == 1, /dependencies/ { next } { print }' | awk '{$1=$1;print}' | awk -F'[=<>:]' '{print $1}' | awk -F'- ' '{print $2}')
for search_term in ${DEPENDENCIES_LIST}; do
  grep -q ^${search_term}$ ${PIP_LIST_FILE}
  [ $? -ne 0 ] && echo "missing conda dependencies/pip: [${search_term}]" && exit 1
done

# Activate default pre-commit hooks
pre-commit install

# Setup env if not available
export PYTHONPATH=./api

python api/main.py
