import os
import discord
from discord.ext import commands

# Configurações de Intents
intents = discord.Intents.defalut()
intents.message_content = True
intents.guilds = True
intents.members = True


class Discordbot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=!, intents=intents, case_insensitive=True,)

    async def startup(self):
        await self.wait_until_ready()
        print(f"{self.user.name} está Online! ")

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"{filename[:-3]} carregado com sucesso")
                except Exception as e:
                    print(
                        f"Falha ao carregar a extensão {filename}.\nErro: {e}")

        self.loop.create_task(self.startup())

    async def on_ready(self):
        activity = discord.Game(name=f"help")
        await self.change_presence(activity=activity)


try:
    bot_instance = Discordbot()
    bot_instance.run(TOKEN)
except discord.LoginFailure:
    print("Erro ao fazer login: Token inválido ou não fornecido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
