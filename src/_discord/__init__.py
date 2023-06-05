"""
The _discord module handles sending messages to users on discord.
It does this by connecting to discord as a bot and sending a direct message (DM)
to another user.
"""

import os
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
pic = None
message = '👀'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    USER_ID = int(os.getenv('DISCORD_RECIPIENT_USER_ID'))
    user = client.get_user(USER_ID)
    # await user.send(pic)
    await user.send(message)
    await client.close()

"""
Removes previous messages from the chat, so that there is only one message at a time.

Not implemented. Delete?
"""
def clear_messages():
    pass

"""
Send the report to the user
:param report: Dictionary
"""
def send_message(message_to_send, pic_to_send=None, do_format=False):
    global pic, message
    message = message_to_send
    
    if do_format:
        message = _format_report(message_to_send)
    
    if pic_to_send:
        pic = pic_to_send

    DISCORD_API_KEY = os.getenv('DISCORD_API_KEY')
    client.run(DISCORD_API_KEY)

"""
Take the weather and todo data and format it into a formatted string.
"""
def _format_report(report):
    # weather data
    weather = report.get('weather')
    message = "👋\nThe temperature will be {}° today. It will be {}° in the morning and {}° in the evening." \
        .format(weather.get('weather_day_temp'),
                weather.get('weather_morn_temp'),
                weather.get('weather_eve_temp'))
    message += "\nFeeling like {}...".format(weather.get('weather_desc'))
    
    # to do data
    todos = report.get('todo')
    if len(todos) > 0:
        message += "\n\nYou have {} events today:".format(len(todos))

        for todo in todos:
            message += '\n* {}'.format(todo.get('summary'))
    else:
        message += "\n\nLooks like you have the day off. Enjoy!"

    return message
