import discord
import random
import requests
import os
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
    await ctx.send('Воспользуйтесь очень важной подсказкой:\n'
                   '$hello - приветствие бота\n'
                   '$add <два произвольных числа> - сложение двух чисел\n'
                   '$heh <количество повторов> - вывод размноженного слова "heh"\n'
                   '$revers <произвольное слово> - вывод слова в обратной последовательности'
                   '$duck - вывод картинки с уткой'
                   '$Deck_of_Cards - вывод игральной карты'
                   '$mem - вывод картинки с мемом')


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_Deck_of_Cards_image_url():
    """Функция возвращает произвольную карту из колоды карт"""

    params = {'count': '1'}
    res = requests.get('https://deckofcardsapi.com/api/deck/new/draw', params=params)

    data = res.json()

    return data['cards'][0]['image']


@bot.command('duck')
async def duck(ctx):
    """По команде duck вызывает функцию get_duck_image_url"""
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('Deck_of_Cards')
async def Deck_of_Cards(ctx):
    """По команде Deck_of_Cards вызывается функция get_Deck_of_Cards_image_url, возвращающая произвольную карта из колоды карт"""
    image_url = get_Deck_of_Cards_image_url()
    await ctx.send(image_url)


@bot.command()
async def mem(ctx):
    lst = os.listdir('images')
    img_name = random.choice(lst)
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)

    # Можем передавать файл как параметр!
    await ctx.send(file=picture)


bot.run("ТУТ УКАЖИТЕ ТОКЕН СВОЕГО БОТА")
