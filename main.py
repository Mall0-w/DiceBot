import discord.py
import os
import Dice

client = discord.Client()

@client.event
async def on_ready():
    print("Hi there! Im tallyBot, you can learn more about me by using $thelp")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #await message.channel.send()
    ''''
  if message.content.startswith('$t'):
    await message.channel.send("Hello world!")
  '''
    if (message.content.startswith("/test")):
        await message.channel.send("this is a test")

client.run(os.getenv('Token'))