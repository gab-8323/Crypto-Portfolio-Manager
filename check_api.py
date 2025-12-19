from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

try:
    print("Testing get_price for bitcoin...")
    price = cg.get_price(ids=['bitcoin'], vs_currencies='usd', include_24hr_change='true')
    print("Price Data:", price)

    print("\nTesting get_coins_markets with sparkline for bitcoin...")
    markets = cg.get_coins_markets(vs_currency='usd', ids=['bitcoin'], sparkline=True, price_change_percentage='24h')
    if markets:
        print(f"Market Data First Item: Name={markets[0]['name']}, Current Price={markets[0]['current_price']}")
        print(f"Sparkline Data Length: {len(markets[0]['sparkline_in_7d']['price'])}")
    else:
        print("Market Data Empty")

except Exception as e:
    print(f"API Error: {e}")
