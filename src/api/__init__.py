import os
from dotenv import load_dotenv
from discord_bot import send_message
from service import generate_report

if __name__ == '__main__':
    load_dotenv()
    # input('send a message?')
    report = generate_report()
    send_message(report)
    # os.system('python discord_bot.py')
