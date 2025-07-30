import os 
from alpaca_trade_api.rest import REST, TimeFrame
# import dotenv 
from dotenv import load_dotenv

load_dotenv()  # load the .env file

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_URL = os.getenv('BASE_URL')

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

account = api.get_account()
print(f"Account status: {account.status}")

# Example: Buy 1 share of AAPL if you have buying power
symbol = "AAPL"
qty = 1

if float(account.buying_power) > 200:
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Market order to buy {qty} share(s) of {symbol} submitted!")
else:
    print("Not enough buying power.")





