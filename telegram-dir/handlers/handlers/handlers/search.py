from telegram import Update
from telegram.ext import CallbackContext
from utils.data_provider import fetch_market_data

def search_command(update: Update, context: CallbackContext):
    try:
        symbol = context.args[0].upper()
        data = fetch_market_data(symbol)
        if data:
            message = (
                f"{data['symbol']} - {data['name']} - Cena: {data['price']}"
                f" - Zmiana: {data['change']:.2f}%"
            )
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Nie znaleziono instrumentu."
            )
    except (IndexError, ValueError):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Użyj: /search <symbol> (np. /search AAPL)",
        )