import ffmpeg
from config import token
import random
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from pretty_help import PrettyHelp

FFMPEG_OPTIONS = {
    'options': '-vn',
}

bot = commands.Bot(command_prefix='-',intents=discord.Intents.all(),help_command=PrettyHelp())


@bot.event
async def on_ready():
    print('бот запустился)')

@bot.command(description='отвечает тебе приветом <3')
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author} , привет я пузо руслана')


@bot.command(description='пузло закатывается в войс')
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send(f'Пузло уже в канале! Попробуйте позже!')
    else:
        voice = await channel.connect()
        await ctx.send(f'Пузло закатилось в канал: {channel}')
        ctx.guild.voice_client.play(discord.FFmpegPCMAudio(source=r'E:\\bot\\tesak.mp3', **FFMPEG_OPTIONS, executable=r"C:\\ffmpeg\\bin\\ffmpeg.exe"))

@bot.command(description='скипает звук который воспроизводится сейчас')
async def skip(ctx):
    if voice!= None and voice:
        voice.stop()
            
def unique_rand(inic: int, lim: int, total: int):
    data = []
    i = 0
    while i < total:
        num = random.randint(inic, lim)
        if num not in data:
            data.append(num)
            i += 1
        laend = len(data)
        laend -= 1 

    return data[laend]

@bot.command(description='говорит смешнявку(БОТ ДОЛЖЕН БЫТЬ В ВОЙСЕ!!!!)')
async def say(ctx):
    meme = [r'E:\\bot\\furion.mp3', r'E:\\bot\\bear.mp3', r'E:\\bot\\anapa).mp3', r'E:\\bot\\kishlak.mp3', r'E:\\bot\\pingvins.mp3', r'E:\\bot\\maw.mp3' , r'E:\\bot\\roblox.mp3']
    mememax = len(meme)
    mememax -= 1
    memerand = unique_rand(0, mememax, 1)
    try:  
        ctx.guild.voice_client.play(discord.FFmpegPCMAudio(source=meme[memerand], **FFMPEG_OPTIONS, executable=r"C:\\ffmpeg\\bin\\ffmpeg.exe"))
    except (TypeError, AttributeError):       
        await ctx.reply('Пузло не в войсе')
    except discord.errors.ClientException:
        await ctx.reply('Пузо уже разговаривает')
        
@bot.command()
async def roblox(ctx):
    ctx.guild.voice_client.play(discord.FFmpegPCMAudio(source=r'E:\\bot\\roblox.mp3', **FFMPEG_OPTIONS, executable=r"C:\\ffmpeg\\bin\\ffmpeg.exe")) #строчка для вадима что бы он помнил че брат с ним может сделать)
    

@bot.command(description='позволяет отдать дань уважения руслану') #память рус
async def pressf(ctx):
    await ctx.reply(f'https://www.youtube.com/watch?v=TtMzTGfs-fc&ab_channel=Cumcrete')
    await ctx.send("Команда в честь памяти руслана, нажмите F to pay respect")

@bot.command(description='пузло выкатывается из войса')
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Пузло выкатилось из: {channel}')
    else:
        await ctx.send('Пузло не в войсе(')
        
@bot.command(description='ролит рандомное число, как в доте короче)')
async def roll(ctx):
    author = ctx.message.author    
    await ctx.reply(f'Вам выпало число: {random.randint(0, 100)}')
    
if __name__ == "__main__":
    bot.run(token) 
    