from telegram import Update
from telegram.ext import CallbackContext
from utils.utils import calculate_fibonacci_levels

def fib_command(update: Update, context: CallbackContext):
    try:
        symbol = context.args[0].upper()
        high = float(context.args[1])
        low = float(context.args[2])
        timeframe = context.args[3].lower()

        levels = calculate_fibonacci_levels(high, low)

        message = f"Poziomy Fibonacciego dla {symbol} ({timeframe}):\n"
        for level, value in levels.items():
            message += f"{level}: {value:.2f}\n"

        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

    except (IndexError, ValueError):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Użyj: /fib <symbol> <high> <low> <timeframe> (np. /fib BTCUSD 68000 60000 4h)",
        )