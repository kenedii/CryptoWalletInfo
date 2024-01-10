import requests
from main import CryptoWalletInfo


class DogecoinWallet(CryptoWalletInfo):

    def get_price(currency='USD'):
        return CryptoWalletInfo.get_price("DOGE", currency).get('DOGE').get(currency)

    def info_dict(address):
        return CryptoWalletInfo.info_dict('doge', address, decimals=100000000)

    def balance_usd(address):
        return DogecoinWallet.get_price() * DogecoinWallet.info_dict(address).get('balance')
