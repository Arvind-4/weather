#!/bin/bash

echo "Upgrade pip..."
python3.9 -m pip install --upgrade pip

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic  --noinput --clear -i admin