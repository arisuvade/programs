#!/bin/bash

echo "Guess the Number!"

number=$(( RANDOM % 10 ))
limit=3

while [[ limit -ne 0 ]]
do
    echo -n "Guess (0-9): "
    read -r guess
    
    if [[ $guess -eq $number ]]; then
        echo "You're correct!"
        exit 0
    else
        limit=$(( limit - 1 ))
        echo "You're wrong!"
    fi
    
done

echo "Out of guesses. Play again."
exit 1
