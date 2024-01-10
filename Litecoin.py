import requests
from main import CryptoWalletInfo


class LitecoinWallet(CryptoWalletInfo):

    def get_price(currency='USD'):
        return CryptoWalletInfo.get_price("LTC", currency).get('LTC').get(currency)


    def info_dict(address):
        return CryptoWalletInfo.info_dict('ltc', address)

    def balance_usd(address):
        return LitecoinWallet.get_price() * LitecoinWallet.info_dict(address).get('balance')

