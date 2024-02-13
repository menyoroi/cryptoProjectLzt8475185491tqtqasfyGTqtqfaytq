from celery import shared_task
from django.core.cache import cache
from django.apps import apps
import time
import ccxt


@shared_task()
def check_crypto_currency():
    cache.set('tickers', {})
    while True:
        try:
            tickers = cache.get('tickers')
            exchange = ccxt.binance()
            markets = exchange.load_markets()
            symbols = list(markets.keys())
            assets = apps.get_model('main', 'Asset').objects.all()
            for asset in assets:
                symbol = f'{asset.short_name}/USDT'
                if symbol in symbols:
                    new_ticker = exchange.fetch_ticker(symbol)
                    tickers[asset.short_name] = new_ticker
            cache.set('tickers', tickers)
        except:
            pass
        time.sleep(5)

