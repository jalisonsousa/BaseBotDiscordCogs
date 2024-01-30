import os
import discord
from discord.ext import commands

# Configurações de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Creating a subclass of commands.Bot
class Discordbot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents, case_insensitive=True)

    # Coroutine to perform tasks when the bot starts up
    async def startup(self):
        await self.wait_until_ready()
        print(f"{self.user.name} está Online!")  # Print a message when the bot is online

    # Coroutine to set up bot hooks and load extensions
    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"{filename[:-3]} loaded successfully")  # Print success message for loading extensions
                except Exception as e:
                    print(f"Failed to load extension {filename}.\nErro: {e}")  # Print error if extension loading fails

        self.loop.create_task(self.startup())

    # Event triggered when the bot is ready
    async def on_ready(self):
        activity = discord.Game(name=f"help")
        await self.change_presence(activity=activity)  # Set the bot's presence to "Playing help"

# Main code
try:
    bot_instance = Discordbot()
    bot_instance.run('YOUR_BOT_TOKEN')  # Run the bot with the provided token
except discord.LoginFailure:
    print("Erro ao fazer login: Token inválido ou não fornecido.")  # Print error if login fails
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")  # Print unexpected errors
