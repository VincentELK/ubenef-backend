#!/bin/bash

clear

echo "========================================="
echo "STARTING TESTS"
echo "========================================="

pytest -v

RESULT=$?

echo "========================================="

if [ $RESULT -eq 0 ]; then
    echo "TESTS SUCCESFULLY PASSED !"
else
    echo "TESTS FAILED !"
fi 

echo "========================================="