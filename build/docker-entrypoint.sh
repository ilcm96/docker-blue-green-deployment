#!/bin/bash

mkdir /app/static && mkdir /app/staticfiles

echo "======Collecting static files======"
python3 manage.py collectstatic --noinput

echo "======Performing database mirgations======"
python3 manage.py migrate

echo "======Starting server======"
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
