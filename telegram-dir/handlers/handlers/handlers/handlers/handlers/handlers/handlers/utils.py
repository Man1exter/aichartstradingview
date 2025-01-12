from utils.data_provider import fetch_market_data
def check_alerts(context,symbol, price_target, condition, user_id):
    data = fetch_market_data(symbol)
    if data:
        current_price = data['price']
        if condition == "powyżej" and current_price > price_target:
              context.bot.send_message(chat_id=user_id, text=f"Osiągnięto alert dla {symbol} Cena: {current_price}")
        elif condition == "poniżej" and current_price < price_target:
              context.bot.send_message(chat_id=user_id, text=f"Osiągnięto alert dla {symbol} Cena: {current_price}")