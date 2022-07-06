import discord
from discord.ext import commands
import os
import requests
import json


bot = commands.Bot(command_prefix='%')
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

  if userMessage.content.startswith('%help'):
    await userMessage.channel.send(unusableRequest)

    #This is an old command line that will be later used to make proper command lines.
#@bot.command()
#async def embed(ctx):
 #rules = discord.Embed(title = "Server Rules", description = "Here are the server rules.", color = discord.Color.green())
 #await ctx.send(rules=rules)
    

@disClient.event
async def on_message(userMessage):
    if userMessage.content.startswith('%rules'):
        embedVar = discord.Embed(title="Server Rules", description="Here are the rules set for the server.", color=0x00ff00)
        embedVar.add_field(name="Rule 1:", value="placeholder", inline=False)
        embedVar.add_field(name="Rule 2:", value="placeholder", inline=False)
        await userMessage.channel.send(embed=embedVar)


disClient.run(os.getenv('KEYTOKEN'))

