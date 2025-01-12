from telegram import Update
from telegram.ext import CallbackContext
from data.database import add_alert,remove_alert,get_alerts
from utils.utils import check_alerts
def alert_command(update: Update, context: CallbackContext):
    try:
        symbol = context.args[0].upper()
        price = float(context.args[1])
        condition = context.args[2].lower()
        user_id = update.effective_user.id
        add_alert(symbol, price, condition, user_id)
        message = f"Alert ustawiony dla {symbol}, cena {condition} {price}"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except (IndexError, ValueError):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Użyj: /alert <symbol> <price> <condition> (np. /alert BTCUSD 66000 powyzej)",
        )


def check_alerts_job(context: CallbackContext):
    alerts = get_alerts()
    for alert in alerts:
        symbol = alert[1]
        price_target = alert[2]
        condition = alert[3]
        user_id = alert[4]
        check_alerts(context,symbol,price_target,condition,user_id)