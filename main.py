import discord
import os
import requests
import json

my_secret = os.environ['KEYTOKEN']

unusableRequest = 'Sorry, no action has been implemented yet ¯\_(ツ)_/¯'

disClient = discord.Client()

@disClient.event
async def on_ready():
 print('Connection Successful {0.user}'.format(disClient))

@disClient.event
async def on_message(userMessage):
  if userMessage.author == disClient.user:
    return

  if userMessage.content.startswith('#help'):
    await userMessage.channel.send(unusableRequest)


disClient.run(os.getenv('KEYTOKEN'))

