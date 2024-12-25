#!/bin/bash

# Start build process
echo "BUILD START"

# Create a virtual environment with Python 3.12
echo "Creating virtual environment..."
python3.12 -m venv env

# Activate the virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Verify virtual environment activation
if [[ "$VIRTUAL_ENV" != "" ]]; then
  echo "Virtual environment activated successfully."
else
  echo "Failed to activate virtual environment!" >&2
  exit 1
fi

# Install dependencies from requirements.txt
echo "Installing dependencies..."
python3.12 -m pip install --upgrade pip setuptools wheel  # Upgrade pip, setuptools, wheel
python3.12 -m pip install -r requirements.txt

# Check if installation was successful
if [[ $? -ne 0 ]]; then
  echo "Failed to install dependencies!" >&2
  exit 1
fi

# Run collectstatic command to gather static files
echo "Running collectstatic..."
python3.12 manage.py collectstatic --noinput

# Check if collectstatic was successful
if [[ $? -ne 0 ]]; then
  echo "Failed to run collectstatic!" >&2
  exit 1
fi

# End build process
echo "BUILD END"
