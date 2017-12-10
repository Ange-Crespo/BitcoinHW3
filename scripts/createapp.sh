#!/bin/bash

echo App name :
read app
cd mysite
python3 manage.py startapp $app