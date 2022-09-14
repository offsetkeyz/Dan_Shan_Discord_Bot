
from discord.ext import commands
 
class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    # '*' is to include everything after command
    # Consume all argument must be last in the function
    async def saymore(ctx, *, message=None):
        if message is None:
            await ctx.send('Please provide a message')
            return
        await ctx.send(f'{message}')

# async 
def setup(bot):
    # await 
    bot.add_cog(BasicCommands(bot))

