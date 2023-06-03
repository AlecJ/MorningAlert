"""
This script is run on boot.

It fetches the machines IP address and sends it to myself via discord.
This is useful since the IP can change occasionally and 
"""

# load env
from dotenv import load_dotenv
load_dotenv()

# load classes
from util.get_ip import get_ip
from _discord import send_message

if __name__ == '__main__':
    pi_ip = get_ip()
    # TODO replace with get_hostname or some such
    pi_ip_message = '[Raspberry Pi] Current IP: {}'.format(pi_ip)
    print(pi_ip_message)

    # send discord message
    send_message(pi_ip_message)