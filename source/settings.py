import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")

FORTNITE_IO_API_SETTINGS = {
    "base_url": "https://fortniteapi.io/",
    "api_key": os.getenv("FORTNITE_IO_KEY"),
    "timeout": 3,
}
