from datetime import datetime
from io import BytesIO

import discord

from source.commands.shop import generate_shop
from source.settings import BOT_TOKEN

client = discord.Client(trust_env=True)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("shop"):
        await message.channel.send(
            file=discord.File(
                BytesIO(generate_shop()), filename=f"shop-{datetime.now()}.png"
            )
        )


client.run(BOT_TOKEN)
