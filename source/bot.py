from datetime import datetime
from io import BytesIO

import discord
from discord.ext import commands

from source.commands.shop import generate_shop
from source.commands.tourneys import get_future_tournaments
from source.settings import BOT_TOKEN


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def shop(ctx):
    data, filename = await generate_shop()
    await ctx.message.channel.send(file=discord.File(BytesIO(data), filename=filename))


@bot.command()
async def tourneys(ctx):
    text = await get_future_tournaments()
    await ctx.message.channel.send(text)


bot.run(BOT_TOKEN)
