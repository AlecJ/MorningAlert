import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
pic = None
message = '👀'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    user = client.get_user(123966857890889728)
    # await user.send(pic)
    await user.send(message)
    await client.close()

def send_message(report):
    """
    :param report: Dictionary
    """
    global pic, message
    pic = report.get('pic_id')
    message = _format_report(report)
    client.run('OTYxNDQwOTgwNTMwMjM3NTEz.Yk5BsA.NINoAD8-7JMDuR65NytYnb8Gxcw')

def _format_report(report):
    """
    Take the weather report data and format it into a list of strings

    report['weather_morn_temp'] = round(weather_data['feels_like']['morn'])
    report['weather_day_temp'] = round(weather_data['feels_like']['day'])
    report['weather_eve_temp'] = round(weather_data['feels_like']['eve'])
    report['weather_desc'] = weather_data['weather'][0]['description']
    report['pic_id'] = weather_data['weather'][0]['icon']
    """
    return "👋\nThe temperature will be {}° today. It will be {}° in the morning and {}° in the evening." \
            .format(report.get('weather_day_temp'),
                    report.get('weather_morn_temp'),
                    report.get('weather_eve_temp')) + "\nFeeling like {}...".format(report.get('weather_desc'))
          
                            
                                        