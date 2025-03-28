#!/bin/bash

# Get the directory path of the current script
script_dir=$(dirname "$(readlink -f "$0")")

# Path to the file in the .venv/bin/ subdirectory
venv_file="$script_dir/.venv/bin/activate"
index_file="$script_dir/index.py"

# Check if the file exists
if [ -f "$venv_file" ]; then
  # Source the file
  source "$venv_file"

  python $index_file

else
  echo "File '$venv_file' not found."
fi

# Example of using variables or functions defined in the sourced file
# (if any)
# echo "Variable from sourced file: $my_variable"
# my_function