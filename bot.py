import json
import sys
from discord.ext import tasks, commands
import random
import discord
import discord.ext
import os
import asyncio
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)
intents = discord.Intents.default()
bot = commands.Bot(commands.when_mentioned_or(config["prefix"]), intents=intents)

TOKEN = config['token']

@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Setup the game status task of the bot
    """
    statuses = ["with screagles!", "with terpic lertning", "with not sleggert"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))

@bot.event
async def on_ready():
    print('Hello!')
    status_task.start()

async def load_cogs() -> None:
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f'cogs.{extension}')
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


asyncio.run(load_cogs())
bot.run(TOKEN)
