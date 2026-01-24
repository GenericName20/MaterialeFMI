#!/bin/bash
read X
read Y
if [ "$X" -lt "$Y" ]; then
    echo "$X e mai mic ca $Y"
else
    echo "$X e mai mare ca $Y"
fi