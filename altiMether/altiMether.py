import ccxt

bleut   = ccxt.bleutrade({
    'apiKey': 'YOUR_API_KEY_HERE',
    'secret': 'YOUR_API_SECRET_KEY_HERE'
    })

bleut_markets = bleut.load_markets()

print(bleut.id, bleut_markets)

print(bleut.fetch_ticker('LTC/ETH'))
print(bleut.fetch_ticker('ETH/BTC'))
print(bleut.fetch_ticker('ETH/DOGE'))
