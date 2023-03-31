#!/bin/bash

if [[ -z $1 || -z $2 ]]; then
    echo "addition: not enough arguments"
else
    z=$(( $1 + $2 ))
    echo "Sum: $z"
fi
