import discord
from discord.ext import commands

# Creating a cog (class) for handling events


class Eventss(commands.Cog):
    def __init__(self, Discordbot):
        self.Discordbot = Discordbot

    # Using a decorator to define a listener for the "on_member_join" event
    @commands.Cog.listener()
    # Event handler for when a member joins the server
    async def on_member_join(self, member):
        # Print a message when a member joins
        print(f'{member.name} has joined the server')

# Async function to set up the cog and add it to the bot


async def setup(Discordbot):
    await Discordbot.add_cog(Events(Discordbot))
