import requests
import pandas as pd
import numpy as np

class DataManager:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3/"

    def get_top_n_cryptos(self, n=10):
        url = f"{self.api_url}coins/markets?vs_currency=usd&order=market_cap_desc&per_page={n}&page=1&sparkline=false"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            df = df[['symbol', 'current_price', 'market_cap']]
            return df
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()

    def get_historical_data(self, crypto_id, days=30):
        url = f"{self.api_url}coins/{crypto_id}/market_chart?vs_currency=usd&days={days}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            prices = np.array(data['prices'])[:,1]
            df = pd.DataFrame({'price': prices})
            return df
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
    
    def get_latest_news(self):
        # Tutaj możesz zaimplementować pobieranie newsów z wybranego źródła (np. za pomocą Beautiful Soup)
        return "Aktualności niedostępne"