# MorningAlert

Daily weather report sent via Discord.

## Set Up

1. Install Requirements

- `cd src && python3 -m virtualenv venv`
- `source venv/bin/activate` (`venv/scripts/activate` for windows)
- `python3 -m pip install -r requirements.txt`

2. Create environment file

- Copy `.env.SAMPLE` and rename it `.env`
- Set `LATITUDE` and `LONGITUDE` to the coordinates you want weather data for
- Obtain an openweather API key from `openweathermap.org` and set `OPEN_WEATHER_API_KEY`

3. Run

- `python3 src/api/__init__.py`

## To Do

Trigger a daily script
Weather Icon
