"""
This script is run on boot.

It fetches the machines IP address and sends it to myself via discord.
This is useful since the IP can change occasionally and 
"""

# load env
from dotenv import load_dotenv
load_dotenv()

# built-ins
import socket

# load classes
from _discord import send_message

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()

    ip_message = '[Raspberry Pi] Current IP: {}'.format(IP)
    print(ip_message)

    # send discord message
    # send_message(ip_message)