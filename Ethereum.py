import requests
from main import CryptoWalletInfo


class EthereumWallet(CryptoWalletInfo):

    def get_price(currency='USD'):
        return CryptoWalletInfo.get_price("ETH", currency).get('ETH').get(currency)

    def info_dict(address):  # This will only give information about the ETH balance
        return CryptoWalletInfo.info_dict('eth', address, decimals=1000000000000000000)

    def balance_usd(address):
        return EthereumWallet.get_price() * EthereumWallet.info_dict(address).get('balance')

    def token_list(address):
        url = f'https://api.ethplorer.io/getAddressInfo/{address}?apiKey=freekey'
        response = requests.get(url)

        if response.status_code == 200:
            # Parse JSON data from the response
            json_data = response.json()
        else:  # If error getting json data
            raise Exception('Wallet address is invalid or ETHPlorer API Endpoint is down.')

        token_list = {}

        for index in range(len(json_data['tokens'])):
            token_address = json_data['tokens'][index]['tokenInfo']['address']  # Token address
            token_name = json_data['tokens'][index]['tokenInfo']['name']  # Token name
            token_symbol = json_data['tokens'][index]['tokenInfo']['symbol']  # Token symbol
            decimals = int("1e" + json_data['tokens'][index]['tokenInfo']['decimals'])  # Number of decimals
            token_price = json_data['tokens'][index]['tokenInfo']['price']['rate']  # Value of token
            address_balance = json_data['tokens'][index]['tokenInfo']['balance'] / decimals  # Amount of token owned
            supply_owned = address_balance / (int(json_data['tokens'][index]['tokenInfo']['totalSupply']) / decimals)  # Percent of total supply owned

            token_info = {'token_name': token_name,
                          'token_symbol': token_symbol,
                          'token_price': token_price,
                          'balance': address_balance,
                          'supply_owned': supply_owned}
            token_list[token_address] = token_info

        return token_list
