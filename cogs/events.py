import discord
from discord.ext import commands, tasks
from itertools import cycle


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
        
    #     # await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))
    #     print('I am here!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server!')

    @commands.Cog.listener()
    async def on_memeber_remove(self, member):
        print(f'{member} has left the server!')


def setup(client):
    client.add_cog((Event(client)))
