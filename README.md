# MorningAlert

Daily weather and todos sent via Discord DM.

## To Do

- finish copy script (copy flow.py to right location)
- copy script needs to create a virtualenv or keep it elsewhere
- copy script needs to copy .env file into dir
- update discord.send_message (sends whatever it gets)
- discord sends message for auth
- cron job to call actions

`google-calendar-secret.json` must be placed in `/src/`

- send IP on startup via discord
- reboot?

### Backlog

- Weather Icon?

## Set Up

A. CI/CD

- github actions

B. Single Install

1. Install Requirements
   This project was developed using Python3.11

- `python3 -m pip install virtualenv` (if you do not have virtualenv installed)
- `python3 -m virtualenv venv`
- `source venv/bin/activate` (`venv/scripts/activate` for windows)
- `python3 -m pip install -r src/requirements.txt`

2. Create environment file

- Copy `.env.SAMPLE` and rename it `.env`
- Set `LATITUDE` and `LONGITUDE` to the coordinates you want weather data for
- Obtain an openweather API key from `openweathermap.org` and set `OPEN_WEATHER_API_KEY`

3. Set up Discord Bot

- ... fill this out?
- Set `DISCORD_API_KEY` with your Discord Bot API Key
- Set `DISCORD_RECIPIENT_USER_ID` to the Discord User ID you want to send reports to

4. Run

- `python3 src/generate_report.py`

## Raspberry Pi Configuration

This should not change, but will be documented here in case something needs to be fixed.

### Structure

The directory structure on the raspberry pi looks like:

```
/home/pi/
    \_ copy.sh
    \_ run.sh
    \_ app/
        \_ .env
        \_ google-calendar-secret.json
        \_ venv/
        \_ MorningAlert/ (repo)
    \_ github-actions-runner/ (github actions -- polls for repo changes)
```

### Cron

To set up cron tasks, edit the crontab with:
`crontab -e`

Copy the contents of ~/deploy/crontab.txt to the open editor.

### Scripts

run.sh - used in cron, runs the daily report
copy.sh - used in cron, copies repo changes from the github actions dir to the app dir
generate_report.py - main script to generate a daily report, sent to me via discord
get_ip.py - used on boot, messages myself on discord with the machines IP
move_unfinished_tasks.py - run at the end of the day, moves remaining todos for today to tomorrow
