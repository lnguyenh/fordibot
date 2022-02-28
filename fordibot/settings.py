import os

import pytz as pytz
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")

FORTNITE_IO_API_SETTINGS = {
    "base_url": "https://fortniteapi.io/",
    "api_key": os.getenv("FORTNITE_IO_KEY"),
    "timeout": 3,
}

# Current season as of February 2022 is 19
CURRENT_SEASON = os.getenv("CURRENT_SEASON", 19)

INTERESTING_EVENTS_KEYWORDS = ["fncs", "duoscash"]
INTERESTING_REGIONS = ["EU", "NAE"]


# Timezones
BASE_TZ = {"name": "SE", "tz": pytz.timezone("Europe/Paris")}
EXTRA_TZ = [{"name": "UK", "tz": pytz.timezone("Europe/London")}]


# Fortnite-shop configuration
# By default, update the shop between 2am and 3am local time
SHOP_REFRESH_HOUR = os.getenv("SHOP_REFRESH_HOUR", 2)
# If set, an image with the content of the fortnit shop will be sent to it periodically
# To get a channel ID, type "\#news" in your server if #news is your target channel
SHOP_CHANNEL_ID = os.getenv("SHOP_CHANNEL_ID")

# Tourney reminder configuration
TOURNEY_REMINDER_PERIOD = 30
