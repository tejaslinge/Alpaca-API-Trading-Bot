import alpaca_trade_api as tradeapi

# authentication and connection details
api_key = 'PK0EWZ57XVTQE1DV60BL'
api_secret = 'd18rJHxyyJS9d9Pp3PxwbGR7OSbzEuxjgs8Z05Qz'
base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)
