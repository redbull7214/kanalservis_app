import requests


def get_rate():
    """Функция получения курса USD."""
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url=url).json()
    usd_rate = response.get('Valute').get('USD').get('Value')
    return float(usd_rate)
