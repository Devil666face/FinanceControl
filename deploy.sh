#!/bin/bash
python -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py collectstatic --no-input
