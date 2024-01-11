# CryptoWalletInfo
All in one Python library to retrieve real time Cryptocurrency Market Info & Wallet Balance information along with fiat conversions. 
Supported chains: BTC, LTC, DOGE, ETH, DASH

This uses Blockcyper API and Ethplorer API. No API tokens are needed.
Historical pricing data is retrieved from Yahoo Finance.

Dependencies: requests, pandas, cryptocompare

Functions:


get_price() Gets the price of a cryptocurrency

info_dict() Returns a dictionary containing information about the wallet and balance

balance_usd() Returns the value of the wallet balance in USD

token_list() Returns a dictionary containing information about the tokens and token balances in a wallet (Supported chains: ETH)

price_history()
Params: 
token = 'BTC', 'ETH','SOL',etc. String, Any crypto tracked on Yahoo Finance
date1='1420117261' String, Unix time no earlier than the first data point on yahoo finance
date2=str(int(time.time())) String, unix time. current date by default. 
interval='1d', String. Options are either '1d', '1wk', or '1mo'
save=True bool. Whether or not to save the file on the machine
Returns:
Pandas Data Frame with price history data
