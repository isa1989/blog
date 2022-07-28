#!/usr/bin/env bash
# pip3 install psycopg2

python manage.py test
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
