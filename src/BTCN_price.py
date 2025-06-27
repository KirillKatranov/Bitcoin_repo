import time
import requests

from queries.orm import if_need_create_tables, insert_data

URL_FOR_BTCN_LATEST_PRICE = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

prices = []
times = []
if_need_create_tables()
while True:
    response = requests.get(URL_FOR_BTCN_LATEST_PRICE).json()
    price = float(response["price"])
    
    prices.append(price)
    insert_data(prices[-1])
    time.sleep(1)

