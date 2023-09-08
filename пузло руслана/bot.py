import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.')


#токен = MTA1MzM2ODQ4OTMzNjg5NzY0Ng.GPNmHI.eIFXqpjl1G-i6wAj_4niXTv9sRRv5Ku0lTJX8I


@client.event

async def on_ready():
    print('пузло здесь')

@client.command(pass_context = True)

async def hello(ctx):
    await ctx.send('Привет, я пузло руслана')

token = open('E:\\пузло руслана\\token.txt', 'r').readline()
client.run(token)