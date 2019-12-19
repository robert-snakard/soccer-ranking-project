#!/usr/bin/env bash

python3 test.py

python3 main.py -f sample_input.txt | diff - expected_output.txt
echo "Testing main with file input - success"

cat sample_input.txt | python3 main.py | diff - expected_output.txt
echo "Testing main with stdin input - success"

echo ""
