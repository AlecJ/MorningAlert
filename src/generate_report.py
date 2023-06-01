"""
This is the main file to be called to generate the daily report.

It fetches the following data and sends it in a formatted message to myself via discord:
- weather data
- any calendar events for today in the "to_do_list" calendar
"""

# load env
from dotenv import load_dotenv
load_dotenv()

# load classes
from _discord import send_message
from weather import get_weather_data
from to_do import get_to_do_data

if __name__ == '__main__':
    report = {}

    # get weather data
    report['weather'] = get_weather_data()

    # get calendar / to-do data
    report['todo'] = get_to_do_data()

    # send discord message
    send_message(report)
