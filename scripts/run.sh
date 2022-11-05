#!/bin/bash
set -e

# Activate default pre-commit hooks
pre-commit install

# Setup env if not available
export PYTHONPATH=./api

python api/main.py
