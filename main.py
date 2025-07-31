import os
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL")

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def buy(symbol, qty):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"✅ BUY order placed: {qty} of {symbol}")
        return order
    except Exception as e:
        print(f"❌ Failed to BUY {symbol}: {e}")
        return None

def sell(symbol, qty):
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"✅ SELL order placed: {qty} of {symbol}")
        return order
    except Exception as e:
        print(f"❌ Failed to SELL {symbol}: {e}")
        return None

def get_account_balance():
        try:
            account = api.get_account()
            return float(account.cash)
        except Exception as e:
            print(f"❌ Failed to get account balance: {e}")
            return 0.0
        



#get_account_balance()

sell("XRP/USD", 1)