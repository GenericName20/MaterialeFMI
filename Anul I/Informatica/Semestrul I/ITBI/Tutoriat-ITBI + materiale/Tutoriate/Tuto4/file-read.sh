#!/bin/bash
I=0
FILENAME="example.txt"

# -r: citeste fara ca backslash (\) sa faca escape
# -p: afiseaza un prompt la utilizator
# -u: citeste dintr-un anumit file descriptor

while read line; do
   I=$(($I+1))
   echo "$I: $line"
done < "$FILENAME"

# Deschide FD 20
exec 20<"$FILENAME"

# < = citire
# > = scriere
# >> = append

while read -u 20 line; do
    echo "Prin FD-ul 20: $line"
done

# Inchide FD 20
exec 20<&-