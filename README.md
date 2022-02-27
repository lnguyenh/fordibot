# Fordibot

## About
This is a Discord bot providing Fortnite goodies to your Discord server. Currently it simply pulls the current items in the item shop and generates an image to the server when it reacts to some keyword.

## Quickstart
### Prepare Discord
You need to register your bot to Discord, and invite the bot to your Discord server. Follow the instructions from https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal . Save the bot token that you will generate for later.

### Get API key access to Fortniteapi.io
This project uses the Fortniteio API. To be able to use it, you need to register here: https://fortniteapi.io/ . Save the api key that you will get for later.
### Prepare Python
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```
### Install wkhtmltopdf
This bot uses the python library `imgkit` to convert html to images. It relies on the well known lightweight program called `wkhtmltopdf` to be installed. Instructions about how to install `wkhtmltopdf`can be found here: https://pypi.org/project/imgkit/ 
### Configuration
You need to create a file called `.env` at the root of this project. Its content should look like:
```
DISCORD_TOKEN="SOME_TOKEN"
FORTNITE_IO_KEY="SOME_API_KEY"
```
### Run the program
```
. ./venv/bin/activate
python source/bot.py
```
