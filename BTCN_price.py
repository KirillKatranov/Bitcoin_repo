import time
import requests

URL_FOR_BTCN_LATEST_PRICE = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

prices = []
times = []


while True:
    response = requests.get(URL_FOR_BTCN_LATEST_PRICE).json()
    price = float(response["price"])
    
    prices.append(price)
    print(prices)
    time.sleep(1)