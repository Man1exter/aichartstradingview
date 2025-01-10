import openai
from config import OPENAI_API_KEY

class AIModule:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def chat_with_ai(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", # lub inny model
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error connecting to AI: {e}"
    
    def get_price_predictions(self, prices):
      # Przykładowa funkcja generująca prognozę
      prompt = f"""
      Based on historical price data: {prices.to_list()},
      Provide a prediction for the price level, the entry and exit prices if you were to trade on the data,
      including a take profit and a stop loss level.
      """
      return self.chat_with_ai(prompt)