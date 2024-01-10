import requests


class CryptoWalletInfo:
    from cryptocompare import get_price

    def info_dict(currency, address, decimals):

        url = f'https://api.blockcypher.com/v1/{currency}/main/addrs/{address}/balance'

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data from the response
            json_data = response.json()
        else:  # If error getting json data
            raise Exception('Wallet address is invalid or Blockcypher API Endpoint is down.')

        info = {'balance': json_data['balance'] / decimals,
                'total_received': json_data['total_received'] / decimals,
                # 'total_spent': json_data['total_spent'] / decimals,
                'n_tx': json_data['n_tx'],  # Number of transactions
                'final_balance': json_data['final_balance']  # Balance + Unconfirmed balance
                }  # Add more keys in the future

        return info
