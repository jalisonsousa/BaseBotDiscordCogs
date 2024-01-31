# BaseBotDiscordCogs
base code to use cogs and does it matter to me, with discord 2.0+

I created this repository with the intention of helping those who are having difficulty creating cogs in their discord bot.
I left some files as an example to base yourself on
- 2 files as example commands
- 1 one called events to put all the events and the model of how it should be followed for it to work
## Cogs in Discord Bots:

  - Cogs are a way to organize and modularize the functionality of a Discord bot.
  - They are implemented as classes that inherit from commands.Cog in the discord.ext.commands extension.
     Each cog class can contain commands and event listeners.

## Commands:
- Commands are actions that the bot can perform in response to user input.
- Each command is implemented as a function within a cog class and is decorated with ```@commands.command()```.

## Event Listeners:
- Event listeners are functions that respond to specific events that occur in the Discord server.
- They are decorated with ```@commands.Cog.listener()```.

## Cogs in the Main Bot File:
- Cogs are loaded and unloaded in the main bot file using the bot instance.
-Loading a cog is typically done with bot.load_extension('cogs.cog_name').

## Setup Function:
- Cogs often include a setup function (e.g., async def setup(bot)), called to add the cog to the bot.
- The setup function is usually invoked from the main bot file.

## Here's a simplified example:

Cog File (cogs/my_cog.py):

<br><br>
# ----------------------------------

# PT / BR

código base para usar cogs e isso importa para mim, com discord 2.0+

Criei este repositório com o intuito de ajudar quem está tendo dificuldade em criar cogs em seu bot do discord.
Deixei alguns arquivos como exemplo para você se basear
- 2 arquivos como comandos de exemplo
- 1 chamado events para colocar todos os eventos e o modelo de como deve ser seguido para funcionar
## cogs em Discord Bots:

  - As cogs são uma forma de organizar e modularizar a funcionalidade de um bot Discord.
  - Eles são implementados como classes que herdam de Commands.Cog na extensão discord.ext.commands.
     Cada classe cog pode conter comandos e ouvintes de eventos.

## Comandos:
- Comandos são ações que o bot pode executar em resposta à entrada do usuário.
- Cada comando é implementado como uma função dentro de uma classe cog e é decorado com ```@commands.command()```.

## Ouvintes de eventos:
- Ouvintes de eventos são funções que respondem a eventos específicos que ocorrem no servidor Discord.
- Eles são decorados com ```@commands.Cog.listener()```.

## cogs no arquivo principal do bot:
- As cogs são carregadas e descarregadas no arquivo bot principal usando a instância do bot.
-O carregamento de uma cogs normalmente é feito com bot.load_extension('cogs.cog_name').

## Função de configuração:
- As cogs geralmente incluem uma função de configuração (por exemplo, async def setup(bot)), chamada para adicionar  cogs ao bot.
- A função de configuração geralmente é invocada a partir do arquivo bot principal.

## Aqui está um exemplo simplificado:
Arquivo Cog (cogs/my_cog.py):
