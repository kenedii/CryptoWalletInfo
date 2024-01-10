import requests
from main import CryptoWalletInfo


class BitcoinWallet(CryptoWalletInfo):

    def get_price(currency='USD'):
        return CryptoWalletInfo.get_price("BTC", currency).get('BTC').get(currency)

    def info_dict(address):
        return CryptoWalletInfo.info_dict('btc',address)

    def balance_usd(address):
        return ( BitcoinWallet.get_price() * BitcoinWallet.info_dict(address).get('balance') )