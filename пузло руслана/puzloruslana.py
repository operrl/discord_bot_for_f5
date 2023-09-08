import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='-')
@bot.event
async def on_ready():
    print('bot started, PUZO ACTIVATED!!!!!')

@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author} Привет я пузо руслана')
    

    await bot.process_commands(message)
    
@bot.command()
async def join(ctx):
    global voice
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