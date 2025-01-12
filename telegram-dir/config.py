import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DEFAULT_TIMEFRAME = "1h"

def load_config():
    return {
        "telegram_bot_token": TELEGRAM_BOT_TOKEN,
        "default_timeframe": DEFAULT_TIMEFRAME,
    }