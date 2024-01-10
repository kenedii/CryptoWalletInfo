import requests

from main import CryptoWalletInfo


class BitcoinWallet():
    def info_dict(address):

        url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data from the response
            json_data = response.json()
        else:  # If error getting json data
            raise Exception('Wallet address is invalid or Blockcypher API Endpoint is down.')

        info = {'balance': json_data['balance'] / 100000000,
                'total_received': json_data['total_received'] / 100000000,
                'total_spent': json_data['total_spent'] / 100000000,
                'n_tx': json_data['n_tx']
                }  # Add more keys in the future

        return info

    def balance_usd(address):
        return CryptoWalletInfo.get_price("BTC") * BitcoinWallet.info_dict(address).balance



BitcoinWallet.get_balance('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
