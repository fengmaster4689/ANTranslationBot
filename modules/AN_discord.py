import discord
from discord.ext import commands
import configparser
from modules.AN_googletrans import *

def bot_events(bot):
    """ 
    creates the events that the bot uses 

    :param bot: the bot instance to assign the events to
    """
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    # @bot.event
    # async def on_message(message):
    #     # Do not let the bot reply to itself or other bots
    #     if message.author == bot.user or message.author.bot:
    #         return

    #     if message.content.startswith('!translate '):
    #         original_text = message.content[len('!translate '):]
    #         translated_text = translate_text_auto(original_text)
    #         await message.channel.send(translated_text)
        
    #     # This line is necessary to process commands
    #     await bot.process_commands(message)

def bot_commands(bot):
    """ 
    creates the commands that the bot uses 

    :param bot: the bot instance to assign the command to
    """
    @bot.command()
    async def hello(ctx):
        """Responds with a simple message."""
        await ctx.send('Hello! I am your bot.')

def bot_initialize(prefix):
    """ 
    initialize the discord bot 

    :param prefix: the symbol character that the bot will use
    """
    
    intents=discord.Intents.default()
    intents.messages = True
    intents.guild_messages = True

    # Create a bot instance with a command prefix
    bot = commands.Bot(prefix, intents=intents)

    # set up event & commands
    bot_commands(bot)
    bot_events(bot)

    return bot

def run_bot():

    # Get prefix from config
    config = configparser.ConfigParser()
    config.read("config.ini")
    prefix = config['Discord']['Prefix']

    # create bot
    bot = bot_initialize(prefix)

    # Get token and run bot
    token = config['Discord']['Token']
    bot.run(token)