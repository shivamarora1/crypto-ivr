import requests
import json
import os


class Coin:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def fetch_price(self):
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={self.symbol}"

        payload = {}
        headers = {
            'X-CMC_PRO_API_KEY': os.getenv('TWILLIO_CALL_KEY')
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == requests.codes.ok:
            obj = response.json()
            return obj['data'][self.symbol]['quote']['USD']['price']
        else:
            print(response.text)
            return "Something went wrong, Please try again later"


class Coins:
    def __init__(self):
        self.__coins = {}

    def add(self, coin: Coin):
        self.__coins[coin.symbol] = coin

    def get(self, coin_symbol: str):
        return self.__coins[coin_symbol]


# global variable
coins = Coins()


def init_coins():
    bitcoin = Coin("Bitcoin", "BTC")
    ethereum = Coin("Ethereum", "ETH")
    tether = Coin("Tether", "USDT")
    doge = Coin("Dogecoin", "DOGE")
    solana = Coin("Solana", "SOL")

    coins.add(bitcoin)
    coins.add(ethereum)
    coins.add(tether)
    coins.add(doge)
    coins.add(solana)
