#!/bin/bash

# Install Tkinter

if [[ -d /etc/pacman.d ]]; then
    if ! sudo pacman -S tk; then
        echo "Error: Failed to install tk package for pacman." >&2
        exit 1
    fi
elif [[ -d /etc/apt ]]; then
    if ! sudo apt-get install python3-tk; then
        echo "Error: Failed to install python3-tk package for apt-get." >&2
        exit 1
    fi
elif [[ -d /etc/yum.repos.d ]]; then
    if ! sudo dnf install python3-tkinter; then
        echo "Error: Failed to install python3-tkinter package for dnf." >&2
        exit 1
    fi
else
    echo "Error: No supported package manager found." >&2
    exit 1
fi

echo "Package installation successful!"


# Install customTkinter
if ! pip install customtkinter; then
    echo "Error: Failed to install customtkinter." >&2
fi

echo "Pip installation successful!"
