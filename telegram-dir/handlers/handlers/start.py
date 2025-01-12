from telegram import Update
from telegram.ext import CallbackContext

def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Witaj! Jestem TradingFibBot. Użyj /help aby zobaczyć dostępne komendy.",
    )

def help_command(update: Update, context: CallbackContext):
    help_text = """
    Dostępne komendy:
    /start - Wyświetla powitanie.
    /help - Wyświetla pomoc.
    /search <symbol> - Wyszukuje instrument.
    /fib <symbol> <high> <low> <timeframe> - Oblicza poziomy Fibonacciego.
    /chart <symbol> <timeframe> - Generuje wykres.
    /alert <symbol> <price> <condition> - Ustawia alert cenowy.
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)