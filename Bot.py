import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Добрый день! Я бот {bot.user}!')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def revers(ctx, word):
    """Функция возвращает слово написанное наоборот"""
    word_revers = ''
    for letter in word[::-1]:
        word_revers = word_revers + letter

    await ctx.send(word_revers)


@bot.command()
async def help_(ctx):
    """Функция возвращает список выполняемых ботом команд"""
    await ctx.send(f'Воспользуйтесь очень важной подсказкой:\n'
                   f'$hello - приветствие бота\n'
                   f'$add <два произвольных числа> - сложение двух чисел\n'
                   f'$heh <количество повторов> - вывод размноженного слова "heh"\n'
                   f'$revers <произвольное слово> - вывод слова в обратной последовательности')


bot.run("ТУТ УКАЖИТЕ ТОКЕН СВОЕГО БОТА")
