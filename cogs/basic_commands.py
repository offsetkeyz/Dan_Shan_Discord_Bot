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
        name="help",
        description="List all commands the bot has loaded."
    )
async def help(self, context: Context) -> None:
    prefix = self.bot.config["prefix"]
    embed = discord.Embed(title="Help", description="List of available commands:", color=0x9C84EF)
    for i in self.bot.cogs:
        cog = self.bot.get_cog(i.lower())
        commands = cog.get_commands()
        data = []
        for command in commands:
            description = command.description.partition('\n')[0]
            data.append(f"{prefix}{command.name} - {description}")
        help_text = "\n".join(data)
        embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
    await context.send(embed=embed)

# async 
def setup(bot):
    # await 
    commands = [help,saymore]
    for command in commands:
        bot.add_command(command)

