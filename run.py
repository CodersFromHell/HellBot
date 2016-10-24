import discord, logging, asyncio, urllib.parse
from discord.ext import commands

description = 'A bot straight from hell!'

bot = commands.Bot(command_prefix='$', description=description)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='UTF-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(' --- ')

bot.run('') 