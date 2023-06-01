#!/bin/sh

cd /home/pi/MorningAlert
. venv/bin/activate
python3 src/generate_report.py

DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"`
echo "$DATE_WITH_TIME: Completed."