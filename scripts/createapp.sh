#!/bin/bash

echo App name :
read app
python3 mysite/manage.py startapp $app