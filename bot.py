import decouple as decouple
import discord
import discord.ext
import os
from b import DSC_TOKEN

from discord.ext import commands
from nslookup import Nslookup

client = commands.Bot(command_prefix=["!", "?", "%"])
domain = "pipi-pupu.sytes.net"
dns_query = Nslookup()

# TODO REMOVE TOKEN BEFORE GITHUB
TOKEN = DSC_TOKEN


@client.event
async def on_ready():
    print('Hello!')


@client.command()
async def gametime(ctx):
    await ctx.send('Game time: 6:30pm PST')


# Valheim Server
@client.command()
async def vserver(ctx):
    ips_record = dns_query.dns_lookup(domain)
    server = str(ips_record.response_full) + " " + str(ips_record.answer)
    await ctx.send("The current IP for our glorious server is " + str(ips_record.answer[0]) + ":2456")


@client.command()
async def beans(ctx):
    await ctx.send(':exploding_head: fuk ur beenz')


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')


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


client.run(TOKEN)
