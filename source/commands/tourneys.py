from datetime import datetime, timezone
from dateutil import parser
import pytz

from source.apis.fortniteio.client import FORTNITE_IO_API_CLIENT
from source.settings import INTERESTING_REGIONS, INTERESTING_EVENTS_KEYWORDS


async def get_future_tournaments():
    tourneys = fetch_tourneys()
    sessions = get_upcoming_sessions(tourneys)
    as_text = format_sessions(sessions)
    return as_text


def format_sessions(sessions):
    text = ""
    paris_tz = pytz.timezone("Europe/Paris")
    london_tz = pytz.timezone("Europe/London")
    for session in sessions:
        text += (
            f"{session['date']}"
            f"  [{session['start'].astimezone(paris_tz).strftime('%H:%M')} "
            f"-{session['end'].astimezone(paris_tz).strftime('%H:%M')}]"
            f"  [UK: {session['start'].astimezone(london_tz).strftime('%H:%M')}"
            f"-{session['end'].astimezone(london_tz).strftime('%H:%M')}]:"
            f"  {session['region']}-{session['line1']}-{session['line2']}\n"
        )
    return text


def get_upcoming_sessions(tourneys, only_interesting=True):
    if only_interesting:
        tourneys = [
            tourney
            for tourney in tourneys
            if tourney["region"] in INTERESTING_REGIONS
            and any(
                [key in tourney["id"].lower() for key in INTERESTING_EVENTS_KEYWORDS]
            )
        ]
    sessions = []
    now = datetime.now(timezone.utc)
    for tourney in tourneys:
        for window in tourney.get("windows", []):
            start_time = parser.parse(window["beginTime"])
            end_time = parser.parse(window["endTime"])
            if end_time > now:
                sessions.append(
                    {
                        "start": start_time,
                        "end": end_time,
                        "date": start_time.date(),
                        "line1": tourney["name_line1"],
                        "line2": tourney["name_line2"],
                        "region": tourney["region"],
                    }
                )

    return sorted(sessions, key=lambda x: x["start"])


def fetch_tourneys():
    tourneys = []
    for region in INTERESTING_REGIONS:
        tourneys.extend(
            FORTNITE_IO_API_CLIENT.get_tournaments(region=region).json()["events"]
        )
    return tourneys
