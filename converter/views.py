from django.shortcuts import render
from django.http import JsonResponse
import requests


def home(request):
    return render(request, 'converter/home.html')


def convert(request):
    if request.method == 'GET':
        amount = float(request.GET.get('amount', 1))
        from_currency = request.GET.get('from_currency', 'USD')
        to_currency = request.GET.get('to_currency', 'EUR')

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if to_currency not in data['rates']:
            return JsonResponse({'error': 'Invalid target currency'})

        rate = data['rates'][to_currency]
        converted_amount = amount * rate

        return JsonResponse({'amount': amount, 'from_currency': from_currency, 'to_currency': to_currency, 'converted_amount': converted_amount, 'rate': rate})
