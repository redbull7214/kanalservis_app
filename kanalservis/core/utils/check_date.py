from datetime import datetime
import telegram


def check_date(supply_date, order_number):
    """Функция отправки сообщения."""

    TOKEN = 'insert token here'
    bot = telegram.Bot(token=TOKEN)
    chat_id = 'chat id here'
    supply_date = datetime.strptime(supply_date, '%d.%m.%Y')
    date_now = datetime.now()
    if date_now > supply_date:
        print(date_now)
        bot.sendMessage(chat_id=chat_id,
                        text=f'У заказа №{order_number} вышел срок поставки')
