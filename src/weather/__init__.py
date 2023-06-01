# from util import loggingFactory
# from util import config
import requests
import os

# _getLogger = loggingFactory('goodmorning.service')


def get_weather_data():
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

    return report


def _get_weather_data():
    """
    open_weather_api_key = 

    # Boston
    # latitude = 42.3876
    # longitude = -71.0995
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
        return response.json().get('daily', [])[0]
    else:
        # logger.error('Request to open weather map failed')
        # raise error, api not working
        raise BaseException('Request to open weather map failed')
