#!/bin/sh
set -e -u

pytest *_test.py
black *.py
flake8 *.py
