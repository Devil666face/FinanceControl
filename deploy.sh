#!/bin/bash
python3.10 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py collectstatic --no-input
