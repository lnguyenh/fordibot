import discord

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

    if message.content.startswith("hello"):
        await message.channel.send("Hello!")


client.run(BOT_TOKEN)
