from discord.ext import commands
import discord
from discord.ext.commands import Context
 
@commands.command()
# '*' is to include everything after command
# Consume all argument must be last in the function
async def say(ctx, *, message=None):
    if message is None:
        await ctx.send('Please provide a message')
        return
    embed = discord.Embed(
            title="Hey, you think you can tell me what to say??",
            description=f"Ok will this make you happy? Dan Shan has been known to say '{message}'",
            color=0x000000
        )
    await ctx.send(embed=embed)

#TODO Send private message to Dan Shan and have him say it in a channel. Message and channel can be parameters.

@commands.command(
    name="userinfo",
    description="Get info on a user"
)
async def userinfo(ctx, user: discord.User):
    await ctx.send(user.display_name + " has earned their place in this clan. You know how...")

# async 
def setup(bot):
    # await 
    commands = [userinfo,say]
    for command in commands:
        bot.add_command(command)

