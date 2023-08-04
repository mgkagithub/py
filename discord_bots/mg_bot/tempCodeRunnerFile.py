import os
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Load the auth application id and token from the bot.env file
dotenv.load_dotenv()
token = os.getenv('token')
client = commands.Bot()
# Create a Discord client

# When the bot is ready, add a listener for the slash command event
@client.event
async def on_ready():
    channel = client.get_channel(1077970125522731021)
    await channel.send('The bot is online ')

@client.slash_command(name="r",description = "gib input" ,  guild_ids=[1018830164102230088]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx,cloud_input):
    talks(cloud_input)
    await ctx.respond(cloud_input)

# Run the bot
client.run(token)
