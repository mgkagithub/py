import os
import dotenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from fbotfunctions import read_file , write_file , lock_status , write_lock_status

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
    if lock_status() == 'unlocked':
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
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")

# display_data , 

@client.command()
async def all_tags(ctx):
    if lock_status() == 'unlocked':            
        data = read_file()
        if data == None or data == 0 or data == {}:
            await ctx.respond("No tags to show.") 
        else:
            await ctx.respond("Current data:")
            for index, (tag, value) in enumerate(data.items(), start=1):
                await ctx.send(f"{index}) {tag}: {value}")
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")
# append_data , 

@client.command()
async def new_tag(ctx,tag,value):
    if lock_status() == 'unlocked':    
        await ctx.respond('Adding tag...')
        data = read_file()
        data[tag] = value
        write_file(data)
        await ctx.respond(f"Your tag {tag} with value {value} has been added :)")
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")
# delete_data , 

@client.command()
async def delete_tag(ctx,index_or_name):
    if lock_status() == 'unlocked':    
        data = read_file()
        role = discord.utils.get(ctx.author.roles, name="staff")
        if role is not None and role.name == "staff":
            await ctx.respond("Gotcha , deleteing tag...")
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
            await ctx.respond("A member tryna run a moderator command XD")
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")

# modify_name ,

@client.command()
async def change_tag_name(ctx,index,new_tag):
    if lock_status() == 'unlocked':
        index = int(index)
        data = read_file()
        role = discord.utils.get(ctx.author.roles, name="staff")
        if role is not None and role.name == "staff":
            await ctx.respond("Gotcha , changing tag name...")
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
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")
# modify_value , 

@client.command()
async def change_tag_value(ctx,index,new_value):
    if lock_status() == 'unlocked':
        index = int(index)
        data = read_file()
        role = discord.utils.get(ctx.author.roles, name="staff")
        if role is not None and role.name == "staff":
            await ctx.respond("Gotcha , changing tag value...")   
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
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")

# delete_all

@client.command()
async def delete_all_tags(ctx,confirm):
    if ctx.author.id == 518118892317442059:
        await ctx.respond("On it sir..")
        if confirm.lower() == 'yes':
            await ctx.send("The set has been deleted.")
            data = {}
            write_file(data)
        else:
            await ctx.send("Operation cancelled.")
    else:
        await ctx.respond("A member/moderator tryna run a Mg command , get denied XD")

@client.command()
async def lock(ctx,status):
    if ctx.author.id == 518118892317442059 and status.lower() == 'lock' and lock_status() == 'unlocked':
        await ctx.respond("locking...")
        write_lock_status('lock')
        await ctx.send("Fueled's bot is now locked for all members")
    elif ctx.author.id == 518118892317442059 and status.lower() == 'unlock' and lock_status() == 'locked':
        await ctx.respond("unlocking...")
        write_lock_status('unlock')
        await ctx.send("Fueled's bot is now unlocked for all members")
    else:
        await ctx.respond("A member/moderator tryna run a Mg command , get denied XD")

@client.command()
async def fueledsd(ctx,confirm):
    if ctx.author.id == 518118892317442059 and confirm.lower() == 'yes':
        await ctx.respond("Shutting down...")
        await ctx.send("Fueled's bot is now offline.")
        await client.close()
    else:
        await ctx.respond("A member/moderator tryna run a Mg command , get denied XD")

@client.command()
async def say(ctx,says):
    if lock_status() == 'unlocked':
        await ctx.respond(says)
    else:
        await ctx.respond("Sorry , i will not be responding to any commands")

@client.command()
async def fueled(ctx):
    await ctx.respond('''Command names and description:\n
    __**Member commands**__
    ```/help``` : Get this message, No parameter\n
    ```/tag``` : Get the value or description of the name or index you provide , parameter - name or index\n
    ```/all_tags``` : Get a list of all tags made in this server, No parameter\n
    ```/new_tag``` : Make a new tag, parameters - tag_name , tag_value\n
    __**Moderator commands**__
    ```/delete_tag``` : Dont like a tag? , just remove it , parameter - index or name of tag\n
    ```/change_tag_name``` : Change only the name of a tag , parameters - index and new_name\n
    ```/change_tag_value``` : Change only the value of a tag , parameters - index and new_value\n''')

# Run the bot

client.run(token)
