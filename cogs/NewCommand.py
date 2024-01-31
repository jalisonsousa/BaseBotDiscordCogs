import discord
from discord.ext import commands


class NewCommands(commands.Cog):
    def __init__(self, Discordbot):
        self.Discordbot = Discordbot

    # commands example
    # To create a new command you must use it like this @commands.command
    @commands.command(aliases=["hi"])
    async def hello(self):
        await ctx.send()


async def setup(Discordbot):
    await Discordbot.add_cog(NewCommands(Discordbot))
