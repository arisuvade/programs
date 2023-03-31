#!/bin/bash

echo "Rock, Paper, and Scissors."
echo -n "Choice: "
read -r _

result=$(( RANDOM % 3 ))

if [[ $result -eq 0 ]]; then
    echo "You won!"
    elif [[ $result -eq 1 ]]; then
    echo "You loss!"
else
    echo "Draw!"
fi
