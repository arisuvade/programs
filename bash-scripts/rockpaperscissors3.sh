#!/bin/bash

echo "Rock, Paper, and Scissors."

result=$(( RANDOM % 3 ))

while true
do
    echo -n "Choice: "
    read -r choice
    
    if [[ $choice != "rock" && $choice != "paper" && $choice != "scissors" ]]; then
        echo "Invalid choice"
        continue
    fi
    
    case $result in
        0)
            echo "You won!"
        ;;
        1)
            echo "You loss!"
        ;;
        *)
            echo "Draw!"
        ;;
    esac
    exit 1
    
done
