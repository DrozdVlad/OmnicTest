import datetime

import requests

from currency.models import Currency


def collect():
    currency_data_json = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json').json()
    for data in currency_data_json:
        Currency.objects.get_or_create(
            code=data['r030'], name=data['txt'], rate=data['rate'], abbreviation=data['cc'],
            exchange_date=datetime.datetime.strptime(data['exchangedate'], '%d.%m.%Y')
        )
