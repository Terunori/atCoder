#!/bin/bash
# download Q and A Data
./ojDl.sh $1
# test your python code
./pythonTest.sh $1
# remove tmp files
rm -f output
rm -rf test