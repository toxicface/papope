# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        "hi"
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'im ' in message.content:
        user = message.content
        user = user.replace('im ', '')
        response = 'Hi ' + user + ', I\'m Ian\'s test bot'
        await message.channel.send(response)

client.run(TOKEN)
