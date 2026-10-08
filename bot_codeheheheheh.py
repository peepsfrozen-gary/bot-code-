import discord
import random
from discord.ext import commands
from bot_logic import gen_pass, flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generation(ctx, pass_length= 10):
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def fahh(ctx):
    await ctx.send(flip_coin())

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def hmmhardchoices(ctx):
    resalt = random.choice(['YES✌️','NO👁️👄👁️'])
    await ctx.send (resalt)

@bot.command()
async def martabak(ctx):
    await ctx.send('martabakmartabakmartabakmartabakmartabakmartabakmartabakmartabakmartabakmartabakmartabak')

@bot.command()
async def hsr(ctx):
    hsrchar = [
        "Evanescia",
        "Blake",
        "Ashveil",
        "Pearl",
        "Heng Heng",
        "March tujuh",
        "Jingliu",
        "Nihilux",
        "Silver Fish",
        "Yao guang"
]
await ctx.send(random.choice(hsrchar))

@bot.command()
async def commands(ctx):
    await ctx.send ('$hello  ,   $heh  ,  $generation  ,  $fahh  ,  $choose  ,  $hmmhardchoices  ,  $martabak  ,  $hsr')
    
bot.run("terserah")
