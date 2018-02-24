#!/bin/bash

for i in `seq 5`
    do
    if [ -e ./test/sample-$i.out ]; then
        printf "test $i\n"
        python $1 <./test/sample-$i.in | tee output
        if [ -e ./test/sample-$i.out ]; then
            diff -u output ./test/sample-$i.out >tmp
            if [ $? -eq 0 ]; then
                printf "\nCOLLECT ANSWER!!\n\n"
            elif [ $? -eq 1 ]; then
                printf "\n--- diff output answer --------------------\n"
                cat tmp
                printf "\nWRONG ANSWER...\n\n"
            fi
            rm tmp
        fi
    fi
    done