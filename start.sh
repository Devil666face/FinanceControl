#!/bin/bash
sudo ./venv/bin/waitress-serve --listen 0.0.0.0:80 config.wsgi:application