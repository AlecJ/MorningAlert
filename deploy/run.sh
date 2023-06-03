#!/bin/sh

if [ -z "$1" ]; then
    echo "Provide a command as an argument."
    echo "Commands: "
    echo "make_report"
    echo "get_ip"
    echo "push_tasks"
    exit 1
fi

cd /home/pi/app
source venv/bin/activate

DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"`

if   [[ $1 == make_report ]]; then
    echo "$DATE_WITH_TIME: Started job: generate_report."
    python src/generate_report.py
elif [[ $1 == get_ip ]]; then
    echo "$DATE_WITH_TIME: Started job: get_ip."
    python src/get_ip.py
elif [[ $1 == push_tasks ]]; then
    echo "$DATE_WITH_TIME: Started job: move_unfinished_tasks."
    python src/move_unfinished_tasks.py
fi

DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"`
echo "$DATE_WITH_TIME: Completed."