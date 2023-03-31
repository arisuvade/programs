#!/bin/bash

if [[ -z $1 || -z $2 ]]; then
    echo "subtraction: not enough arguments"
else
    z=$(( $1 - $2 ))
    echo "Difference: $z"
fi
