from datetime import datetime
from io import BytesIO

import discord
from discord.ext import commands, tasks

from source.commands.shop import generate_shop
from source.commands.tourneys import get_future_tournaments, get_tourney_reminder
from source.settings import (
    BOT_TOKEN,
    SHOP_REFRESH_HOUR,
    SHOP_CHANNEL_ID,
    BASE_TZ,
    TOURNEY_REMINDER_PERIOD,
)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    periodic_shop.start()
    tourney_reminder.start()


@bot.command()
async def shop(ctx):
    data, filename = await generate_shop()
    await ctx.message.channel.send(file=discord.File(BytesIO(data), filename=filename))


@bot.command()
async def tourneys(ctx):
    text = await get_future_tournaments()
    await ctx.message.channel.send(text)


@tasks.loop(minutes=60.0)
async def periodic_shop():
    if not SHOP_CHANNEL_ID:
        return
    if datetime.now(BASE_TZ["tz"]).hour == SHOP_REFRESH_HOUR:
        data, filename = await generate_shop()
        channel = bot.get_channel(int(SHOP_CHANNEL_ID))
        await channel.send(file=discord.File(BytesIO(data), filename=filename))


@tasks.loop(minutes=TOURNEY_REMINDER_PERIOD)
async def tourney_reminder():
    text = await get_tourney_reminder()
    if text:
        channel = bot.get_channel(int(SHOP_CHANNEL_ID))
        await channel.send(text)


bot.run(BOT_TOKEN)
