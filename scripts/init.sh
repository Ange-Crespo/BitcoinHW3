#!/bin/bash

cd mysite && python3 manage.py runserver & sleep 0.5 && xdg-open http://127.0.0.1:8000/currencies/init



