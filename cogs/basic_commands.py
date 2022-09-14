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
        # name="help",
        # description="List all commands the bot has loaded."
    )
async def helpp(self, context: Context) -> None:
    print('pp')

# async 
def setup(bot):
    # await 
    commands = ['helpp','saymore']
    for command in commands:
        bot.add_command(command)

