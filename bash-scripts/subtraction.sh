#!/bin/bash

echo -n "Minuend: "
read -r x
echo -n "Subtrahend: "
read -r y

z=$(( x - y ))
echo "Difference: $z"
