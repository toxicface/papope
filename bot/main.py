import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
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
