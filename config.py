import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from mylegram.org/apps
API_ID = int(getenv("API_ID", "27833866"))
API_HASH = getenv("3648a12e9a8df3f448d4aeaac2ab91ab")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7844653451:AAHGRoUmEfDmqgbVRbBEdvFZzMboPcukVl4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5743632846))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://t.me/ramowlfbio",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/emremusicbotkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/emremusicbotgrup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("AgGotgoAEBda_BCuUO0ckvqQdQIhThGKuCAN1WdUrND2-NGB-_wdcGwumDQoUJXecCRnlQBMubCdiWc2fkbYpfjuZauFZIPpOHKhPrTmuHmiQg-fCYb7H7FaEFXUv8MMO7Xew0xe2Id6UHpYE8CTIdaKqOEyYDgLeUWheFctdHyCIzB4BybfVqUEHa4trTdQF1asEYBu5nhl-a5ODrBwgXgFzNgASlIBj3z_u0f5RgRe1QiNE89UF7OE-LbLLUvXOFM29f_i5LbH9MC9iZlyg8VXrhyxHT_qBg_R9Zndcww-S8CjpfuN-lloPvPs-qeRsbwIV-fSNOznHM3gzZ0gOu66IXq7ZgAAAAFWWOHOAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Yeni-11-29"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Yeni-11-29"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"
STATS_IMG_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Eski-11-29"
STREAM_IMG_URL = "https://telegra.ph/Eski-11-29"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Eski-11-29"
YOUTUBE_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
