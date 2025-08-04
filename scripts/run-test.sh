#!/bin/bash

cd "$(dirname "$0")/.." && ./python3-virtualenv/bin/python -m unittest discover -v tests/