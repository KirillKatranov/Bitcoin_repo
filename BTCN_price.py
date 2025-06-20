import time
import matplotlib
import requests
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
URL_FOR_BTCN_LATEST_PRICE = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

prices = []
times = []

plt.ion()  # Включаем интерактивный режим (обновление без нового окна)
fig, ax = plt.subplots()


while True:
    response = requests.get(URL_FOR_BTCN_LATEST_PRICE).json()
    price = float(response["price"])
    
    prices.append(price)
    times.append(len(prices))  # просто индекс вместо времени

    ax.clear()  # очищаем старый график
    ax.plot(times, prices, label="BTC/USDT", color="blue", marker='o')
    ax.set_title("Текущая цена BTC")
    ax.set_xlabel("Тики (секунды)")
    ax.set_ylabel("Цена, $")
    ax.grid(True)
    ax.legend()

    plt.pause(1)  # обновление графика каждые 1 сек
