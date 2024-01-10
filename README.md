# CryptoWalletInfo
All in one Python library to retrieve real time Cryptocurrency wallet balance information along with USD conversions. 
Supported chains: BTC, LTC, DOGE, ETH

Dependencies: pip install cryptocompare, requests

Functions:
get_price() Gets the price of a cryptocurrency
info_dict() Returns a dictionary containing information about the wallet and balance
balance_usd() Returns the value of the wallet balance in USD
token_list() Returns a dictionary containing information about the tokens and token balances in a wallet (Supported chains: ETH)
