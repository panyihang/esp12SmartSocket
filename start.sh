#!/bin/bash
systemctl start mariadb.service
systemctl start docker.service
python py/saveMQTTMsg.py &
python django/manage.py runserver 0.0.0.0:8000 & 
