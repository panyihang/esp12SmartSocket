#!/bin/bash
systemctl start mariadb.service
python py/saveMQTTMsg.py &
