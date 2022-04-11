# from util import loggingFactory
# from util import config
from datetime import datetime
import requests
import csv
import os

# _getLogger = loggingFactory('goodmorning.service')


"""
"""


def generate_report():
    """
    Compile all data for a daily report, including weather data from
    openweather, calendar events from google calendar, and a random
    message from the DB.
    :return: Dict - weather, events, and message data
    """
    report = {}
    
    # get weather data
    weather_data = _get_weather_data()
    report['weather_morn_temp'] = round(weather_data['feels_like']['morn'])
    report['weather_day_temp'] = round(weather_data['feels_like']['day'])
    report['weather_eve_temp'] = round(weather_data['feels_like']['eve'])
    report['weather_desc'] = weather_data['weather'][0]['description']
    report['pic_id'] = weather_data['weather'][0]['icon']
    
    # get user's calendar events
    # _get_calendar_events()

    return report


def _get_weather_data():
    """
    open_weather_api_key = 

    # Boston
    # latitude = 42.35843
    # longitude = -71.05977
    """
    # logger = _getLogger('_get_weather_data')
    # logger.info('testing get weather data')
    api_uri = "https://api.openweathermap.org/data/2.5/onecall"
    api_key = os.getenv('OPEN_WEATHER_API_KEY')
    latitude = os.getenv('LATITUDE')
    longitude = os.getenv('LONGITUDE')

    # request open weather data
    response = requests.get(api_uri, params = {
        'units': 'imperial',
        'lat': latitude,
        'lon': longitude,
        'APPID': api_key,
    })

    # response ok?
    if response.status_code == 200:
        return response.json()['daily'][0]

    else:
        # logger.error('Request to open weather map failed')
        # raise error, api not working
        raise BaseException('Request to open weather map failed')


def _get_calendar_events():
    test = "https://www.googleapis.com/calendar/v3/users/me/calendarList/"
    api_uri = "https://calendar.google.com/calendar/embed?src=alecbjordan%40gmail.com&ctz=America%2FNew_York"
    params = {
        'timeMin': datetime.now().isoformat(),
        'showDeleted': false,
        'singleEvents': true,
        'maxResults': 10,
        'orderBy': 'startTime'
    }