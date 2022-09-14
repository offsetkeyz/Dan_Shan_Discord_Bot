import json
import sys
from discord.ext import tasks, commands
import random
import discord
import discord.ext
import os
import asyncio
from discord.ext import commands
from nslookup import Nslookup

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

client = commands.Bot(command_prefix=config['prefix'])

TOKEN = config['token']

@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Setup the game status task of the bot
    """
    statuses = ["with screagles!", "with terpic lertning", "with not sleggert"]
    await client.change_presence(activity=discord.Game(random.choice(statuses)))

@client.event
async def on_ready():
    print('Hello!')
    status_task.start()

@client.command()
# '*' is to include everything after command
# Consume all argument must be last in the function
async def say(ctx, *, message=None):
    if message is None:
        await ctx.send('Please provide a message')
        return
    await ctx.send(f'{message}')

@client.command()
async def userinfo(ctx, user: discord.User):
    await ctx.send(user.display_name + " has earned their place in this clan. You know how...")

# Multiple Arguments
@client.command()
async def multi(ctx, role: discord.Role, user: discord.User):
    await ctx.send(role.id)
    await ctx.send(user.id)

async def load_cogs() -> None:
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await client.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")



asyncio.run(load_cogs())
client.run(TOKEN)
