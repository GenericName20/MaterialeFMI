#!/bin/bash
read X
case "$X" in
    1)
        echo "X este 1"
        ;;
    2)
        echo "X este 2"
        ;;
    *)
        echo "Nu e nici 1 nici 2"
        ;;
esac