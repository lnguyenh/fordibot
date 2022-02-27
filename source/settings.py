import os
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

INTERESTING_EVENTS_KEYWORDS = ["fncs"]
INTERESTING_REGIONS = ["EU", "NAE"]
