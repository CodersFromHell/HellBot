import discord, logging, asyncio, urllib.parse
from discord.ext import commands
from functions import *
from data import permission

level = levels.Level()

description = 'A bot straight from hell!'

bot = commands.Bot(command_prefix='$', description=description)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='UTF-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
perm = permission.Permission("conf/permission.json")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(' --- ')
    # for each user
    # look up user in server
    # if not registered, add them in database

@bot.async_event
async def on_message(msg):
    content = msg.content
    member = msg.author
    await level.on_message(bot, msg)
    perms = member.server_permissions
    #c_user = user.CustomUser.fromMember()

bot.run('token')
