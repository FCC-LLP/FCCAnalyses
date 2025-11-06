#!/bin/bash

# signal or background
mode=$1

if [ -z "$mode" ]; then
    echo "Usage: $0 signal|background"
    exit 1
fi

rm -f queue.txt

for job in {0..99}; do
    if [ "$mode" == "signal" ]; then
        for mass in 1.0; do         
            for cme in 365; do   
                echo "$cme $mass 10000 $job"
            done
        done
    elif [ "$mode" == "background" ]; then
        for cme in 365; do
            echo "$cme 10000 $job"
        done
    else
        echo "ERROR: Unknown mode '$mode' (use 'signal' or 'background')"
        exit 1
    fi
done > queue.txt