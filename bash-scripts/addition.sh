#!/bin/bash

echo -n "Addend: "
read -r x
echo -n "Addend: "
read -r y

z=$(( x + y ))
echo "Sum: $z"
