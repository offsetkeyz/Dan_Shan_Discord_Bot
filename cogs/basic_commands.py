import aiohttp
import discord
from discord.ext import commands
 
class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
# '*' is to include everything after command
# Consume all argument must be last in the function
async def say(ctx, *, message=None):
    if message is None:
        await ctx.send('Please provide a message')
        return
    await ctx.send(f'{message}')

@commands.command()
async def userinfo(ctx, user: discord.User):
    await ctx.send(user.display_name + " has earned their place in this clan. You know how...")


async def setup(bot):
    await bot.add_cog(BasicCommands(bot))

