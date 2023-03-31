#!/bin/bash

echo "Rock, Paper, and Scissors."
echo -n "Choice: "
read -r choice

if [[ $choice != "rock" && $choice != "paper" && $choice != "scissors" ]]; then
    echo "Invalid choice"
    exit 1
fi

result=$(( RANDOM % 3 ))

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
