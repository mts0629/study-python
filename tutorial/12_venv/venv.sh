#!/bin/bash -eu

# Create virtualenv
python3 -m venv .venv

# Activate vitrualenv
source .venv/bin/activate

# Install package by pip
python -m pip install numpy

# Install package with specific version
python -m pip install requests==2.6.0

# Upgrade package to the latest
python -m install --upgrade requests

# Uninstall package
python -m pip uninstall numpy

# Show package info
python -m pip show requests

# Show the list of installed packages
python -m pip list

# Show the list of installed packages
# with the format for pip install
python -m pip freeze > requirements.txt
cat requirements.txt

# Install packages by requirements.txt
# python -m pip install -r requirements.txt

# Deactivate virtualenv
deactivate
