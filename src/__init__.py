import os
from dotenv import load_dotenv
load_dotenv()
from _discord import send_message
from weather import get_weather_data
from to_do import get_to_do_data

if __name__ == '__main__':
    # input('send a message?')
    report = {}

    # get weather data
    report['weather'] = get_weather_data()

    # get calendar / to-do data
    report['todo'] = get_to_do_data()

    # send discord message
    send_message(report)
    # os.system('python discord_bot.py')
