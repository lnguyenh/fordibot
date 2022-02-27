# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/ghost.svg" card_color="#40DBB0" width="50" height="50" style="vertical-align:middle"/> Fordibot

## About
Discord bot providing Fortnite-related commands to your Discord server.

Credits and resources:
* **Discord.py:** https://discordpy.readthedocs.io/en/stable/index.html
* **Fortnite IO API:** https://fortniteapi.io/

## Commands
### !shop
Pulls the item shop via API, generates a summary image and posts it in Discord
### !tourneys
Posts a summary containing all upcoming tournaments. Preferred regions and type of tournaments can be configured.

## Quickstart
### Prepare Discord
You need to register your bot to Discord, and invite the bot to your Discord server. Follow the instructions from https://discordpy.readthedocs.io/en/stable/discord.html . Save the bot token that you generate for later.

### Get an API key for Fortniteapi.io
This project uses the Fortniteio API. To be able to use it, you need to register here: https://fortniteapi.io/ . Save the api key that you get for later.

### Prepare Python
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

### Install wkhtmltopdf
This bot uses the python library `imgkit` to convert html to images. It relies on the lightweight program `wkhtmltopdf` to be installed. Instructions about how to install `wkhtmltopdf`can be found here: https://pypi.org/project/imgkit/ 

### Configuration
You need to create a file called `.env` at the root of this project. Its content should look like:
```
DISCORD_TOKEN="SOME_TOKEN"
FORTNITE_IO_KEY="SOME_API_KEY"
```
Check the file `settings.py` for more configuration parameters. Look for lines containing `os.getenv()`

### Run the program
```
. ./venv/bin/activate
python source/bot.py
```
