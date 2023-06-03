#!/bin/sh

rsync -a --delete /home/pi/github-actions-runner/_work/MorningAlert/MorningAlert /home/pi/app/
cp /home/pi/github-actions-runner/_work/MorningAlert/MorningAlert/deploy/pip.pi.txt /home/pi/app/
cd /home/pi/app/
source venv/bin/activate
pip install -r pip.pi.txt
cp /home/pi/github-actions-runner/_work/MorningAlert/MorningAlert/deploy/flow.py /home/pi/app/venv/lib/python3.9/site-packages/google_auth_oauthlib/flow.py