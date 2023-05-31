#!/bin/sh

cd /home/pi/MorningAlert
. venv/bin/activate
python3 src/api/__init__.py

DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"`
echo "$DATE_WITH_TIME: Completed."