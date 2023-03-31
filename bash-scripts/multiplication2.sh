#!/bin/bash

if [[ -z $1 || -z $2 ]]; then
    echo "multiplication: not enough arguments"
else
    z=$(( $1 * $2 ))
    echo "Product: $z"
fi
