import discord
from discord.ext import commands


class Intro(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def intro(self, ctx):
        await ctx.send('I am a Primitive Bot! lol')


def setup(client):
    client.add_cog((Intro(client)))
