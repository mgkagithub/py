import pyttsx3
import os
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands

def talks(input):
    input = str(input)
    # Initialize the text-to-speech engine.
    engine = pyttsx3.init()

    # Set the voice.
    engine.setProperty('voice', 'english-us')

    # Say some text.
    engine.say(input)

    # Play the speech.
    engine.runAndWait()

# Load the auth application id and token from the bot.env file
dotenv.load_dotenv()
token = os.getenv('TOKEN')
client = commands.Bot()
# Create a Discord client

# When the bot is ready, add a listener for the slash command event
@client.slash_command(name="r",description = "gib input" ,  guild_ids=[1018830164102230088]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx,cloud_input):
    talks(cloud_input)
    await ctx.respond(cloud_input)

# Run the bot
client.run(token)
