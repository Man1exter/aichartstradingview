import requests
from config import load_config
import json
#API key from polygon.io
API_KEY = "YOUR_POLYGON_API_KEY"
BASE_URL = "https://api.polygon.io/v3/"

def fetch_market_data(symbol):
    url = f"{BASE_URL}ticker/{symbol}?apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
           price_data = get_last_price(symbol)
           if price_data:
              return {
                 "symbol": symbol,
                 "name": data["results"]["name"],
                 "price":price_data,
                 "change": price_data - data["results"]["prevDay"]["c"],
              }
        else:
          return None
    return None

def get_last_price(symbol):
      url = f"{BASE_URL}trades/{symbol}?limit=1&apiKey={API_KEY}"
      response = requests.get(url)
      if response.status_code == 200:
        data = response.json()
        if data.get("results"):
           return data["results"][0]["price"]
      return None



def fetch_historical_data(symbol, timeframe):
      if timeframe == "1h":
            multiplier = 1
            timespan = "hour"
      elif timeframe =="4h":
            multiplier = 4
            timespan = "hour"
      elif timeframe =="1d":
          multiplier = 1
          timespan = "day"
      else:
          return None
      url = f"{BASE_URL}aggs/ticker/{symbol}/range/{multiplier}/{timespan}/2024-01-01/2024-01-20?adjusted=true&sort=asc&limit=500&apiKey={API_KEY}"
      response = requests.get(url)
      if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            return data["results"]
      return None