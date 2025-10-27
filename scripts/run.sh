#!/bin/bash

# Launch script for Localhost Monitor

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Add project to PYTHONPATH
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

# Run the app
python -m src.main

echo "App exited. Press any key to close..."
read -n 1
