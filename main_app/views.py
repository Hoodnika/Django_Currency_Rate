from datetime import datetime

import pytz
import requests
from django.http import JsonResponse
from django.shortcuts import render

from main_app.models import CurrencyRate


def get_current_usd(request):
    # Сохраняем последние 10 запросов курсов
    last_rates = CurrencyRate.objects.all().order_by('-date')[:10]
    time_diff = (datetime.now(pytz.utc) - last_rates[0].date).total_seconds()

    # делаем проверку последнего запроса более 10 секунд
    if time_diff >= 10:
        api_url = 'https://open.er-api.com/v6/latest/USD'
        response = requests.get(api_url)
        data = response.json()

        CurrencyRate.objects.create(
            rate=data['rates']['RUB'],
            currency_from=data['base_code'],
            currency_to='RUB',
        )

        result = {
            'currency_from': data['base_code'],
            'rate': data['rates']['RUB'],
            'currency_to': 'RUB',
            'last_rates': [{
                'date': r.date,
                'currency_from': r.currency_from,
                'rate': r.rate,
                'currency_to': r.currency_to
            } for r in last_rates]
        }
    else:
        result = {
            'currency': last_rates[0].currency_from,
            'rate': last_rates[0].rate,
            'currency_to': 'RUB',
            'last_rates': [{
                'date': r.date,
                'currency_from': r.currency_from,
                'rate': r.rate,
                'currency_to': r.currency_to
            } for r in last_rates]
        }
    return JsonResponse(result)
