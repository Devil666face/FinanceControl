#!/bin/bash
./venv/bin/waitress-serve --listen 127.0.0.1:8002 config.wsgi:application