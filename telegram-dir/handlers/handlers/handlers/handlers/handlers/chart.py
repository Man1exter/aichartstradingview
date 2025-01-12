from telegram import Update
from telegram.ext import CallbackContext
from utils.data_provider import fetch_historical_data
from data.charts import generate_line_chart

def chart_command(update: Update, context: CallbackContext):
    try:
        symbol = context.args[0].upper()
        timeframe = context.args[1].lower()

        historical_data = fetch_historical_data(symbol, timeframe)

        if historical_data:
            chart_file = generate_line_chart(historical_data)
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=open(chart_file, "rb"),
                caption=f"Wykres dla {symbol} ({timeframe})",
            )
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Nie można pobrać danych do wykresu.",
            )
    except (IndexError, ValueError):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Użyj: /chart <symbol> <timeframe> (np. /chart AAPL 1d)",
        )