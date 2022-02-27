from datetime import datetime
from io import BytesIO

import discord
from discord.ext import commands

from source.commands.shop import generate_shop
from source.settings import BOT_TOKEN


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith("hello bot"):
        await message.channel.send("Hello human!")

    if message.content.startswith("shop"):
        await message.channel.send(
            file=discord.File(
                BytesIO(generate_shop()), filename=f"shop-{datetime.now()}.png"
            )
        )


bot.run(BOT_TOKEN)
