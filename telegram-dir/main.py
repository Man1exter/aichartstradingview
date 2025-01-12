import logging
from telegram.ext import Updater, CommandHandler
from config import load_config
from handlers import start, search, fibonacci, chart, alert

def main():
    config = load_config()
    token = config["telegram_bot_token"]

    if not token:
        print("Błąd: Brak tokena bota. Ustaw 'TELEGRAM_BOT_TOKEN' w .env")
        return

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Dodawanie handlerów
    dispatcher.add_handler(CommandHandler("start", start.start_command))
    dispatcher.add_handler(CommandHandler("help", start.help_command))
    dispatcher.add_handler(CommandHandler("search", search.search_command))
    dispatcher.add_handler(CommandHandler("fib", fibonacci.fib_command))
    dispatcher.add_handler(CommandHandler("chart", chart.chart_command))
    dispatcher.add_handler(CommandHandler("alert", alert.alert_command))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()