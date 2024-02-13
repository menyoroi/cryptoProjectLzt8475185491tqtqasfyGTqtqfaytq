from django.test import TestCase
import ccxt

# Инициализация объекта биржи (в данном случае Binance)
exchange = ccxt.binance()

symbol = 'BTC/USDT'
ticker = exchange.fetch_ticker(symbol)
print(ticker)

# Получение полного списка валют
markets = exchange.load_markets()

"""# Вывод списка валют
currencies = list(markets.keys())
print("Список валют:")
for currency in currencies:
    print(currency)"""
