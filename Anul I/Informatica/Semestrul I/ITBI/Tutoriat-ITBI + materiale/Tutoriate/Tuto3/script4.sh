#!/bin/bash
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    echo "Pentru nr. $i:"
    if [ $(($i%3)) = "0" ]; then
        echo "Fizz"
    fi
    if [ $(($i%5)) = "0" ]; then
        echo "Buzz"
    fi
done