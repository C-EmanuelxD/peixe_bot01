import discord
import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token_disc = os.getenv('TOKEN_KEY')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='px!', intents=intents)

@bot.event
async def on_read():
    print(f"Bot logado como {bot.user}")
    print(f"HORA DE ODIAR O RAFAEL PORRA!")

@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá {ctx.author.mention}! Você é um bosta mas o rafael é pior xdd")

@bot.command()
async def maicon(ctx):
    img = "image.png"

    msg = """
6x Municipal de racha ilegal (2022) 🏆🏆🏆🏆🏆🏆
9x Estadual de corrida de rua (2023) 🏆🏆🏆🏆🏆🏆🏆🏆🏆
4x BBB Turcomenistão (2018) 🏆🏆🏆🏆
2x Soletrando (2012) 🏆🏆
3x Prisão estadual de Corumbá (2024) 🏆🏆🏆
3x Largados e Pelados (2019, 2020) 🏆🏆🏆
2x Racha na BR 251 (2020) 🏆🏆
2x Melhor jogador interperiodos (2024) 🏆🏆
1x Exposed no twitter (2019) 🏆
1x Craque do dia "Donos da bola" (2017) 🏆
1x Campeonato Mineiro (2018) 🏆
1x Teleton (2017) 🏆
2x Criança esperança (2017) 🏆🏆
5x Melhor jogador de tigrinho (2024) 🏆🏆🏆🏆🏆
1x Lider Avião da Blaze (2024) 🏆
1x Arrancada 400mts Juiz de Fora (2015) 🏆
2x Copa pistão (2016, 2019) 🏆🏆
2x Motor rajado AP 1.8 (2025) 🏆🏆
1x Cavalo de pau na porta do STF (2024) 🏆
2x "Comprou ganhou" do Celso Portiolli (2021, 2022) 🏆🏆
4x Queda de bicicleta (2018, 2019, 2020, 2021) 🏆🏆🏆🏆
1x Bike roubada (2023) 🏆
2x Triatlo de Los santos até Paleto Bay (2022) 🏆🏆
1x Dono do morro (2023) 🏆
🥇 Top 1 Mundial Military Tycoon Roblox (2022)
🥇 Top 1 Mundial Build Battle Hylex (2015)
🥇 Top 1 Mundial Bedwars Hylex (2016)
🥇 Top 10 Counter Blox (2018)"""
    await ctx.send(msg)
    await ctx.send(file=discord.File("image.png"))

@bot.command()
async def rafael(ctx):
    await ctx.send(f"É a pior pessoa que esse mundo já viu, o anticristo, forjado nas chamas do scat e viciado em ser corno")

@bot.command()
async def saidera(ctx):
    await ctx.send(f"Saidera proclamada com sucesso! (quitar antes nao vale)")

@bot.command()
async def horse(ctx):
    await ctx.send("vaco")
    await ctx.send(file=discord.File("vaco1.png"))
    await ctx.send(file=discord.File("vaco2.png"))
    await ctx.send(file=discord.File("vaco3.png"))
    await ctx.send(file=discord.File("vaco4.png"))
    await ctx.send(file=discord.File("vaco5.png"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

    id_rafael = 1211528103365705779

    ctx = await bot.get_context(message)

    if ctx.command is None and message.author.id == id_rafael:
        await message.channel.send(f'Vai se foder {message.author.mention} leproso')

keep_alive()

bot.run(token_disc)