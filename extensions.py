import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Нельзя перевести одинаковые валюты "{quote}".')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не смог обработать валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не смог обработать валюту {quote}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не смог обработать количество "{amount}".')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = amount * json.loads(r.content)[keys[quote]]

        return total_base