#!/bin/bash

echo -n "Multiplicand: "
read -r x
echo -n "Multiplier: "
read -r y

z=$(( x * y ))
echo "Product: $z"
