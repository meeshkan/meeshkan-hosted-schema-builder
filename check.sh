#!/bin/sh
set -e -u

isort *.py
pytest *_test.py
black *.py
flake8 *.py
