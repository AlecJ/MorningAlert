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
    
    # mantra
    mantra = report.get('mantra')
    if mantra:
        message += "\n\n" + mantra

    return message