import os
import sys
import configparser
import discord
from discord.ext import commands
from modules.AN_googletrans import *

def bot_events(bot):
    """ 
    creates the events that the bot uses 

    :param bot: the bot instance to assign the events to
    """
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

def bot_commands(bot):
    """ 
    creates the commands that the bot uses 

    :param bot: the bot instance to assign the command to
    """
    @bot.command()
    async def hello(ctx):
        """Responds with a simple message."""
        await ctx.send('Hello! I am your bot.')

    @bot.command()
    async def translate(ctx, *, text: str):
        """Translates the provided text and sends it back."""
        translated_text = translate_text_auto(text)
        await ctx.send(translated_text)

def bot_initialize(prefix):
    """ 
    initialize the discord bot 

    :param prefix: the symbol character that the bot will use
    """
    
    intents=discord.Intents.all()
    intents.messages = True
    intents.guild_messages = True

    # Create a bot instance with a command prefix
    bot = commands.Bot(prefix, intents=intents)

    # set up event & commands
    bot_commands(bot)
    bot_events(bot)

    return bot

def get_token(config):
    """ 
    gets the discord token from ini or env

    :param config: the config file to try and get the token
    """
    token = config['Discord']['Token']
    if (token == 'PASTE_BOT_TOKEN_HERE'):
        token = os.getenv('DISCORD_BOT_TOKEN')
        if token == None:
            exit("discord token could not be retrieved \nplease edit config.ini or add the bot token to env")
            raise SystemExit
    return token

def run_bot():

    # Get prefix from config
    config = configparser.ConfigParser()
    config.read("config.ini")
    prefix = config['Discord']['Prefix']

    # create bot
    bot = bot_initialize(prefix)

    # Get token and run bot
    token = get_token(config)
    bot.run(token)