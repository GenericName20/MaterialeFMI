#!/bin/bash
# $((expresie)) -> evaluare expresii aritmetice
# $(comanda) SAU `comanda` -> evaluare comanda
read N
I=0
while [ "$I" -lt "$N" ]; do
    echo "$I"
    I=$(($I+1))
done;