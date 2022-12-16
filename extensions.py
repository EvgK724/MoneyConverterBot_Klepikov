import requests
import json
from config import keys


class APIException(Exception):
    pass


class MoneyConverter:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise APIException(f'Нельзя выполнить конвертацию одноименных валют {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]*amount
        total_base = round(total_base, 2)

        return total_base


