import aiohttp
import discord
import asyncio
from discord.ext import commands
 
class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(BasicCommands(bot))

