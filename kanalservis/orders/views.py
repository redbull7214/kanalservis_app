import os
from django.shortcuts import render
from .models import Order
from core.utils.sheets import read_sheets
from core.utils.converter import get_rate
from core.utils.check_date import check_date


def index(request):
    """Представление главной страницы."""
    CREDENTIALS_FILE = os.path.dirname(__file__) + "/templates/kanal.json"
    data = read_sheets(CREDENTIALS_FILE)
    Order.objects.all().delete()
    total_price_usd = 0
    usd_rate = get_rate()
    for item in data:

        price_in_rubs = int(item[2]) * usd_rate
        supply_date = item[3]
        order_number = item[1]
        """Перед разкомментированием необходимо подставить данные в core.utils.check_date"""
        # check_date(supply_date, order_number)
        Order.objects.create(number=item[0], order_number=order_number,
                             price_in_dollars=item[2], price_in_rubs=price_in_rubs, supply_date=supply_date)
        total_price_usd += int(item[2])

    obj = Order.objects.all()
    total_price_rub = int(total_price_usd * usd_rate)
    context = {
        "obj": obj,
        "total_price_usd": total_price_usd,
        "total_price_rub": total_price_rub,
    }
    return render(request, 'index.html', context)
