#!/bin/bash

cd mysite && python3 manage.py crontab $1 $2
