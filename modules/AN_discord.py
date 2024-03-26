import os
import sys
import configparser
import discord
from discord.ext import commands
from modules.AN_googletrans import *

bAutoTranslate: bool = False
bAutoTranslateUser = []
bAutoTranslateChannel = []

def bot_events(bot):
    """ 
    creates the events that the bot uses 

    :param bot: the bot instance to assign the events to
    """
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.event
    async def on_message(message):
        # Do not let the bot reply to itself or other bots
        if bAutoTranslate and (message.channel.id in bAutoTranslateChannel):
            if message.author == bot.user or message.author.bot:
                print("bot message, ignored")
                return
            print(f"reading: {message}")
            translatedText = translate_text_auto(message)
            if(translatedText):
                await message.channel.send(translatedText)
            
        # Important: This line is necessary to process commands
        await bot.process_commands(message)

def bot_commands(bot):
    """ 
    creates the commands that the bot uses 

    :param bot: the bot instance to assign the command to
    """
    @bot.command()
    async def translate(ctx, *, text: str):
        """Translates the provided text and sends it back."""
        translatedText = translate_text_auto(text)
        if(translatedText):
            await ctx.send(translatedText)

    @bot.command()
    async def enable_auto_translate(ctx, *, flag: bool):
        global bAutoTranslate 
        bAutoTranslate = flag
        await ctx.send(f"auto translate set to {bAutoTranslate}")

    @bot.command()
    async def enable_channel(ctx, *, id: str):
        global bAutoTranslateChannel
        id = int(id[2:-1]) #remove the <# prefix and > suffix
        print(id)
        for channel in ctx.guild.channels:
            print(channel.id)
            if channel.id == id:
                bAutoTranslateChannel.append(id)
                await ctx.send(f"added channel: {channel.name}")
                break
        

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