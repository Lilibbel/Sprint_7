from collections import namedtuple
import random
from datetime import datetime, timedelta

OrderData = namedtuple('OrderData', [
    'firstName',
    'lastName',
    'address',
    'metroStation',
    'phone',
    'rentTime',
    'deliveryDate',
    'comment',
    'color'
])


def generate_order_data(color=None):
    if color is None:
        color = []

    return OrderData(
        firstName="Тест",
        lastName="Тестов",
        address="Москва, ул. Тестовая, 1",
        metroStation=random.randint(1, 10),
        phone=f"+7999{random.randint(1000000, 9999999)}",
        rentTime=random.randint(1, 7),
        deliveryDate=(datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d"),
        comment="Тестовый заказ",
        color=color
    )