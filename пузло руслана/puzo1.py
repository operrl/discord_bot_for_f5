import discord
from discord.ext import commands
from discord.utils import get
import random

bot = commands.Bot(command_prefix='-')
@bot.event
async def on_ready():
    print('ruslan online, runaway pls')


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author} Привет я пузо руслана')
    a = get('')

@bot.command()
async def start(ctx):
    global voice
    channel = 
    voice = get(bot.voice_clients, guilds = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Пузло закатилось в канал: {channel}')


@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guilds = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Пузло закатилось в канал: {channel}')

@bot.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)
    

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Пузло выкатилось из: {channel}')
    else:
        voice = await channel.connect()
        await ctx.send(f'Пузло выкатилось из: {channel}')






bot.run('MTA1MzM2ODQ4OTMzNjg5NzY0Ng.GPNmHI.eIFXqpjl1G-i6wAj_4niXTv9sRRv5Ku0lTJX8I')

