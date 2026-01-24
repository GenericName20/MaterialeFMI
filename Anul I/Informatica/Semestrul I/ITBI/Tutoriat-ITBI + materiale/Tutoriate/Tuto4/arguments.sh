#!/bin/bash
# in C -> in shell
# argc = $#
# argv[i] = $i
# argv[7] = $7
# argv[12] = ${12}
# in shell: comanda shift

echo "Hello, $0!"
echo "Vom gasi $# argumente"

I=0
while [[ "$1" != "" ]]; do
    I=$(($I+1))
    echo "Argumentul $I: $1"
    shift
done