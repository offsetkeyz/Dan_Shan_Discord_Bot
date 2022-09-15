from cmath import log
import json
import sys
import traceback
from discord.ext import tasks, commands
from discord.ext.commands import Context
import random
import discord
import discord.ext
import os
import platform
import asyncio
from discord.ext import commands

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)
intents = discord.Intents.default()
bot = commands.Bot(commands.when_mentioned_or('!'), intents=intents)

TOKEN = config['token']

@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Setup the game status task of the bot
    """
    statuses = ["with screagles!", "with terpic lertning", "with not sleggert"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))

@tasks.loop(minutes=1)
async def cogs_reload() -> None:
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.reload_extension(f'cogs.{extension}')
            except Exception as e:
                return

#TODO Handle exceptions cleanly. Maybe logging or printing to console.
@bot.event
async def on_message(message: discord.Message) -> None:
    """
    The code in this event is executed every time someone sends a message, with or without the prefix

    :param message: The message that was sent.
    """
    try:
        await bot.process_commands(message)
    except Exception as e:
        print('error test line 76 bot.py')

@bot.event
async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """
        # All other Errors not returned come here. And we can just print the default TraceBack.
        print('''
        ---------------
        Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr''')
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        print("---------------")

@bot.event
async def on_ready():
    """
    The code in this even is executed when the bot is ready
    """
    print(f"Logged in as {bot.user.name}")
    print(f"discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    status_task.start()
    cogs_reload.start()

# async def load_cogs() -> None:
#     """
#     The code in this function is executed whenever the bot will start.
#     """
#     for file in os.listdir(f"./cogs"):
#         if file.endswith(".py"):
#             extension = file[:-3]
#             try:
#                 # await 
#                 bot.load_extension(f'cogs.{extension}')
#                 print(f"Loaded extension '{extension}'")
#             except Exception as e:
#                 exception = f"{type(e).__name__}: {e}"
#                 print(f"Failed to load extension {extension}\n{exception}")

async def load_cogs() -> None:
    """
    The code in this function is executed whenever the bot will start.
    """
    for file in os.listdir(f"./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

asyncio.run(load_cogs())
bot.run(TOKEN)



