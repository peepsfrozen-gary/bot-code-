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

@bot.command ('get_tips')
async def helpme (ctx, how_many:int):
    tipsandtrik = [
        'Beli martabak dari sumber lokal supaya mengurangi biaya transportasi',
        'Mendaur ulang botol plastik lama daripada membuangnya',
        'Gunakan barang yang dapat digunakan kembali untuk mengurangi penggunaan barang sekali pakai',
        'Pelajari tentang daur ulang dan bahan apa saja yang dapat didaur ulang',
        'Hemat air, jangan menyalakan keran jika tidak dipakai',
        'Cobalah untuk menggunakan transportasi umum, sepeda, dan berjalan kaki (jika memungkinkan) daripada menggunakan mobil',
        'Gunakan peralatan hemat energi di rumah, seperti bola lampu dan AC'
    ]
    await ctx.send('\n'.join(random.choices(tipsandtrik, k= how_many)))

def get_waste_type(waste):
    #standarisasi inputan
    waste = waste.lower().strip()
    non_recyclable_waste = ["food scraps", "dirty tissue", "diaper", "cigarette butt", "styrofoam"]
    recyclable_waste = ["plastic bottle", "plastic cup", "glass bottle", "newspaper", "cardboard", "can"]

    if waste in recyclable_waste:
        return "this is recyclable waste"
    elif waste in non_recyclable_waste:
        return "this is non-recyclable waste" 
    else:
        return "this isn't a waste, dont throw it"

@bot.command()
async def waste_type(ctx, *, waste:str):
    type_waste = get_waste_type(waste)

    await ctx.send(type_waste)
    
bot.run("terserah")
