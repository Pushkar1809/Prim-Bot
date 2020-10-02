import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
import json


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return(prefixes[str(message.guild.id)])


client = commands.Bot(command_prefix=get_prefix)
status = cycle(['$help', 'just fkin around XD', 'Ask me anything! lol'])


@client.event
async def on_ready():
    change_status.start()
    # await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))
    print('I am here!')


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    print(f'joined {guild}')


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    print(f'removed from {guild}')


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to {prefix}')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded successfully!')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded successfully!')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded successfully!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')
