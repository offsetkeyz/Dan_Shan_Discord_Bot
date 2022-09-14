from discord.ext import commands
import discord
from discord.ext.commands import Context
 
@commands.command()
# '*' is to include everything after command
# Consume all argument must be last in the function
async def saymore(ctx, *, message=None):
    if message is None:
        await ctx.send('Please provide a message')
        return
    await ctx.send(f'{message}')

@commands.command(
    name="userinfo",
    description="Get info on a user"
)
async def userinfo(ctx, user: discord.User):
    await ctx.send(user.display_name + " has earned their place in this clan. You know how...")

# async 
def setup(bot):
    # await 
    commands = [userinfo,saymore]
    for command in commands:
        bot.add_command(command)

