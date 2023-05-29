import os
from dotenv import load_dotenv
# from discord import send_message
# from weather import get_weather_data
from to_do import get_to_do_data

if __name__ == '__main__':
    load_dotenv()
    print('ok')
    print(os.environ['CALENDAR_ID'])
    # input('send a message?')

    # get weather data

    # get calendar / to-do data
    # to_do_data = get_to_do_data()
    
    # weather_data = get_weather_data()





    # send_message(report)
    # os.system('python discord_bot.py')
