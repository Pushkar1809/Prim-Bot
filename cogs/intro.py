import discord
from discord.ext import commands


class Intro(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def intro(self, ctx):
        await ctx.send('I am a Primitive Bot! lol')

    @commands.command()
    async def embedhelp(self, ctx):

        helpEmbed = discord.Embed(
            colour=discord.Colour.gold(),
            title="A bot in need is a Bot indeed",
            description="Your favourite Primbot is here for your help. \n\nFollow the following instructions to help me help you by letting you help yourself. \nDamn it was tough"
        )
        helpEmbed.set_author(
            name="Author", icon_url="https://thispersondoesnotexist.com/image")
        helpEmbed.set_thumbnail(
            url="https://picsum.photos/200/300")
        helpEmbed.add_field(
            name="At your disposal!", value="I reckon you need my help sire!", inline=False)
        helpEmbed.add_field(name="Following are the functional comands",
                            value="""
                            \n8ball: command `ask`
                            Introductory: 
                                    1. command `intro`: I introduce myself
                                    2. command `embedhelp`: I feel my help is needed. Bye!!! :man_running:
                            Administration: 
                                    1. command `kick`: The forbidden action
                                    2. command `ban`: Needed for Tik Tok
                                    3. command `unban`: For those who ** "really changed" **
                            """, inline=False)
        helpEmbed.set_footer(
            text="Hope you like my service! Ta ta. \nContribution from github.com/jayeshbhole")

        await ctx.send(embed=helpEmbed)


def setup(client):
    client.add_cog((Intro(client)))
