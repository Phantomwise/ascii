#!/bin/bash

# Check if a file was provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Check if the provided argument is a valid file
if [ ! -f "$1" ]; then
    echo "Error: $1 is not a valid file."
    exit 1
fi

# Read the file and display it with color formatting
while IFS= read -r line; do
    echo -e "$line"
done < "$1"
