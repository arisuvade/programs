#!/bin/bash

echo "Guess the Number!"
echo -n "Guess (0-9): "
read -r guess

number=$(( RANDOM % 10 ))

if [[ $guess -eq $number ]]; then
    echo "You're correct!"
else
    echo "You're wrong!"
fi
