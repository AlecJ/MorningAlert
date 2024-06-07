"""
The _discord module handles sending messages to users on discord.
It does this by connecting to discord as a bot and sending a direct message (DM)
to another user.
"""

import os
import discord
import asyncio
from .util import _format_report


class DiscordClient(discord.Client):
    """
    This discord client is designed to respond to events. In this case,
    we want to start the client, perform it's actions, and close immediately.

    For this reason, we need to set a bunch of values in the __init__, notably
    `message` which is what will be sent to the user.
    """
    def __init__(self, wait_for_response=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = int(os.getenv('DISCORD_RECIPIENT_USER_ID'))
        self.fetched_user = None
        self.message = None
        self.do_wait_for_response = wait_for_response
        self.response = None

    """
    Called once the client has connected to the discord servers.

    Either simply send a message and close or send a message and poll for a response.
    """
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.send_message(self.message)
        
        if self.do_wait_for_response:
            await self.wait_for_response()

        await self.close_client()

    """
    Sends a message to user.
    """
    async def send_message(self, message):
        if self.fetched_user is None:
            self.fetched_user = await self.fetch_user(self.user_id)

        await self.fetched_user.send(message)

    """
    Polls for a direct message response from the user and returns it.
    """
    async def wait_for_response(self):
        await self.send_message('pls respond')

        def check(m):
            return m.author.id == self.user_id and isinstance(m.channel, discord.DMChannel)

        try:
            msg = await self.wait_for('message', check=check, timeout=30.0)  # Timeout can be adjusted as needed
            self.response = msg.content
        except asyncio.TimeoutError:
            self.response = "No response received within the timeout period."

    """
    Closes the client. Necessary for cleanup.
    """
    async def close_client(self):
        await self.close()


"""
Send the report to the user
:param message: Dictionary - 
:param do_format: Bool - should this dict message be formatted as a good morning report.
:
"""
async def asyncio_send_message(message, do_format=False, wait_for_response=False):
    intents = discord.Intents.default()
    intents.members = True
    client = DiscordClient(intents=intents, wait_for_response=wait_for_response)

    if do_format:
        client.message = _format_report(message)
    else:
        client.message = message

    await client.start(os.getenv('DISCORD_API_KEY'))

    #
    if wait_for_response:
        return client.response

"""
Entry point for sending message (asynchronous) from a synchronous process.
"""
def send_message(message, do_format=False,  wait_for_response=False):
    return asyncio.run(asyncio_send_message(message, do_format, wait_for_response))
