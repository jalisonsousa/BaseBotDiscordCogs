import discord
from discord.ext import commands
from config import *


class AdminComandos(commands.Cog):
    def __init__(self, Discordbot):
        self.Discordbot = Discordbot

    # commands example
    # To create a new command you must use it like this @commands.command
    @commands.command(aliases=["id"])
    @commands.has_permissions(administrator=True)
    async def get_id(self, ctx, member: discord.Member = None):
        """get id user"""
        if not member:
            return await ctx.send("Please mention a user for information.")

        user_name = f"{member.name}#{member.discriminator}"
        user_id = member.id

        embed = discord.Embed(
            title="Informações do Usuário",
            description=f"**Nome:** {user_name}\n**ID do Usuário:** {user_id}",
            color=discord.Color.blue()
        )

        await ctx.send(embed=embed)

    @get_id.error  # For errors, the logic is the same as the old models
    async def id_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")


async def setup(Discordbot):
    await Discordbot.add_cog(AdminComandos(Discordbot))
