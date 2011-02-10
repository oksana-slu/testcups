#!/usr/bin/bash

python manage.py printmod contact 2> $(date +'%Y-%m-%d').log
