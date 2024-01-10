import requests
from main import CryptoWalletInfo


class DashWallet(CryptoWalletInfo):

    def get_price(currency='USD'):
        return CryptoWalletInfo.get_price("DASH", currency).get('DASH').get(currency)

    def info_dict(address):
        return CryptoWalletInfo.info_dict('dash',address, decimals=100000000)

    def balance_usd(address):
        return ( DashWallet.get_price() * DashWallet.info_dict(address).get('balance') )
