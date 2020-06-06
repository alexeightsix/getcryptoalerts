import re
import requests
import json
from flask import jsonify


class Coin:

    def __init__(self):
        self.api_endpoint = "https://pro-api.coinmarketcap.com/v1/cryptocurrency"
        self.api_auth = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '',
        }

    def get(self, symbol) -> float:
        #parameters = {'start': '1', 'limit': '1'}
        #request = requests.get(f"{self.api_endpoint}/map", headers=self.api_auth, data=parameters)
        pass

    def all(self):
        parameters = {'start': '1', 'limit': '9999'}
        request = requests.get(
            f"{self.api_endpoint}/map", headers=self.api_auth, data=parameters)
        data = request.json()
        return jsonify(list(map(lambda coin: {'name': coin['id'], 'symbol': coin['symbol']}, data['data'])))
