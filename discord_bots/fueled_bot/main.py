import os
import csv
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
# Load the auth application id and token from the bot.env file
dotenv.load_dotenv()
token = os.getenv('FUELED_TOKEN')
messages_list = []
# Create a Discord client

client = discord.Bot(command_prefix='f.',intents=discord.Intents.all())

# tag handler

filename ="C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.txt"
cmd_dict = {}
with open(filename, 'r') as data:
  for line in data.readlines():
    num = line.split('-')
    num,val = num[0],num[1]
    for i in val:
        val = val.replace("\n","")
        val = val.replace("'","")
    cmd_dict[num] = val

# When the bot is ready, add a listener for the slash command event
# cmds to add - add tag , edit tag , check lb , delete tag , currency system

@client.event
async def on_ready():
   await client.get_channel(1113683858664202320).send("Fueled's bot is now online <:chocosips:1098105097499705424>")

@client.command()
async def tag(ctx,tag_name):
    a = cmd_dict.keys()
    if tag_name in a:
        await ctx.respond(cmd_dict[tag_name])
    else:
        await ctx.respond(f"Sorry , that tag name doesnt exist.\nTry using any of the following:- {a}")

@client.command()
async def all_tags(ctx):
    a = cmd_dict.keys()
    print(a)
    await ctx.respond(a)

@client.command()
async def say(ctx,says):
    await ctx.respond(says)
# Run the bot
client.run(token)
