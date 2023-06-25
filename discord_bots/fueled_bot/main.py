import os
import csv
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from fbotfunctions import read_file , write_file

# Load the auth application id and token from the bot.env file

dotenv.load_dotenv()
token = os.getenv('FUELED_TOKEN')
messages_list = []

# Create a Discord client

client = discord.Bot(command_prefix='f.',intents=discord.Intents.all(), activity = discord.Game(name="/fueled"),status=discord.Status.dnd)

@client.event
async def on_ready():
   await client.get_channel(1113683858664202320).send("Fueled's bot is now online <:chocosips:1098105097499705424>")
activity = discord.Activity(type=discord.ActivityType.listening, name="/fueled")
# command tags

@client.command()
async def tag(ctx,index_or_tag):
    data = read_file()
    tags = list(data.keys())
    if index_or_tag.isdigit():
        index = int(index_or_tag)
        if index >= 1 and index <= len(tags):
            tag = tags[index - 1]
            value = data[tag]
            await ctx.respond(value)
        else:
            await ctx.respond("Invalid index.")
    else:
        if index_or_tag in tags:
            value = data[index_or_tag]
            await ctx.respond(value)
        else:
            await ctx.respond("Invalid tag name.")

# display_data , 

@client.command()
async def all_tags(ctx):
    data = read_file()
    if data == False:
       await ctx.respond("No tags to show.") 
    else:
        await ctx.respond("Current data:")
        for index, (tag, value) in enumerate(data.items(), start=1):
            await ctx.send(f"{index}) {tag}: {value}")

# append_data , 

@client.command()
async def new_tag(ctx,tag,value):
    await ctx.respond('Adding tag...')
    data = read_file()
    data[tag] = value
    write_file(data)
    await ctx.respond(f"Your tag {tag} with value {value} has been added :)")

# delete_data , 

@client.command()
async def delete_tag(ctx,index_or_name):
    data = read_file()
    role = discord.utils.get(message.author.roles, name="staff")
    if role is not None and role.name == "staff":
        data = read_file()
        tags = list(data.keys())
        if index_or_name.isdigit():
            index = int(index_or_name)
            if index >= 1 and index <= len(tags):
                tag = tags[index - 1]
                del data[tag]
                write_file(data)
                await ctx.respond(f"Tag '{tag}' deleted successfully.")
            else:
                await ctx.respond("Invalid index.")
        else:
            if index_or_name in tags:
                del data[index_or_name]
                write_file(data)
                await ctx.respond(f"Tag '{index_or_name}' deleted successfully.")
            else:
                await ctx.respond("Invalid tag name.")
    else:
        await ctx.respond("A member tryna run a moderator command lol")

# modify_name ,

@client.command()
async def change_tag_name(ctx,index,new_tag):
    data = read_file()
    role = discord.utils.get(message.author.roles, name="staff")
    if role is not None and role.name == "staff":
        await ctx.respond("Gotcha , changing tag name")
        data = read_file()
        tags = list(data.keys())
        if index >= 1 and index <= len(tags):
            tag = tags[index - 1]
            value = data.pop(tag)
            data[new_tag] = value
            write_file(data)
            await ctx.respond(f"Tag '{tag}' changed successfully.")
        else:
            await ctx.respond("Invalid index.")
    else:
        await ctx.respond("A member tryna run a moderator command , get denied XD")

# modify_value , 

@client.command()
async def change_tag_value(ctx,index,new_value):
    data = read_file()
    role = discord.utils.get(message.author.roles, name="staff")
    if role is not None and role.name == "staff":
        await ctx.respond("Gotcha , changing tag value")   
        data = read_file()
        tags = list(data.keys())
        if index >= 1 and index <= len(tags):
            tag = tags[index - 1]
            data[tag] = new_value
            write_file(data)
            await ctx.respond(f"Value of tag '{tag}' changed successfully.")
        else:
            await ctx.respond("Invalid index.")
    else:
        await ctx.respond("A member tryna run a moderator command , get denied XD")

# delete_all

@client.command()
async def delete_all_tags(ctx,confirm):
    if ctx.author.id == 518118892317442059:
        await ctx.respond("On it sir..")
        if confirm.lower() == 'yes':
            await ctx.send("The set has been deleted!")
            data = {}
            write_file(data)
        else:
            await ctx.send("Operation cancelled.")
    else:
        await ctx.respond("A member/moderator tryna run a Mg command , get denied XD")

# @client.command()
# async def all_tags(ctx):

# @client.command()
# async def all_tags(ctx):


@client.command()
async def say(ctx,says):
    await ctx.respond(says)

@client.command()
async def fueled(ctx):
    await ctx.respond('''Command names and description:\n
    __**Member commands**__
    ```/help``` : Get this message, No paramter\n
    ```/tag``` : Get the value or description of the name or index you provide , paramter - name or index\n
    ```/all_tags``` : Get a list of all tags made in this server, No paramter\n
    ```/new_tag``` : Make a new tag, paramters - tag_name , tag_value\n
    __**Moderator commands**__
    ```/delete_tag``` : Dont like a tag? , just remove it , paramter - index or name of tag\n
    ```/change_tag_name``` : Change only the name of a tag , paramters - index and new_name\n
    ```/change_tag_value``` : Change only the value of a tag , paramters - index and new_value\n
    __**Bot Owner Only**__
    ```/delete_all_tags``` : Mg only''')

# Run the bot

client.run(token)
