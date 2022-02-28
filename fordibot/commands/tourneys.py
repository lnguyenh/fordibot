from datetime import datetime, timezone, timedelta
from dateutil import parser

from fordibot.apis.fortniteio.client import FORTNITE_IO_API_CLIENT
from fordibot.settings import (
    INTERESTING_REGIONS,
    INTERESTING_EVENTS_KEYWORDS,
    BASE_TZ,
    EXTRA_TZ,
    TOURNEY_REMINDER_PERIOD,
)


def get_future_sessions():
    tourneys = fetch_tourneys()
    sessions = get_upcoming_sessions(tourneys)
    return sessions


async def get_future_tournaments():
    sessions = get_future_sessions()
    as_text = format_sessions(sessions)
    return as_text


def display_time(t, tz):
    return f"{t.astimezone(tz).strftime('%H:%M')}"


def format_sessions(sessions):
    text = ""
    for session in sessions:
        text += (
            f"{session['date']}"
            f"  [{display_time(session['start'], BASE_TZ['tz'])}"
            f"-{display_time(session['end'], BASE_TZ['tz'])}]"
        )
        for extra_tz in EXTRA_TZ:
            text += (
                f"  [{extra_tz['name']}: {display_time(session['start'], extra_tz['tz'])}"
                f"-{display_time(session['end'], extra_tz['tz'])}]:"
            )
        text += f"  {session['region']}-{session['line1']}-{session['line2']}\n"
    return text


async def get_tourney_reminder():
    text = ""
    sessions = get_future_sessions()
    now = datetime.now(BASE_TZ["tz"])
    for session in sessions:
        start_time = session["start"]
        delta = start_time - now
        if delta < timedelta(minutes=TOURNEY_REMINDER_PERIOD) and now < start_time:
            delta_in_minutes = int(delta.seconds / 60)
            text += (
                f"**Reminder:** "
                f"  {session['region']}-{session['line1']}-{session['line2']} starts in {delta_in_minutes} minutes \n"
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
