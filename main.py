import discord
import os
import messageHandler

client = discord.Client()

@client.event
async def on_ready():
    print("Hello World!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #await message.channel.send()
    ''''
  if message.content.startswith('$t'):
    await message.channel.send("Hello world!")
  '''
    temp = messageHandler.messageHandler(message)
    if temp != None:
      await message.channel.send(temp)
    


client.run(os.getenv('Token'))