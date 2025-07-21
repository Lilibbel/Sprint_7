from collections import namedtuple
import requests
import random
import string
from config import URLs

# Изменим имя поля на first_name (с нижним подчеркиванием)
CourierData = namedtuple('CourierData', ['login', 'password', 'first_name'])


def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def register_new_courier_and_return_login_password():
    # Используем first_name в данных для API (как требует документация)
    data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()  # Здесь оставляем как есть для API
    }

    response = requests.post(URLs.COURIER, data=data)
    if response.status_code == 201:
        # При создании CourierData используем first_name (с подчеркиванием)
        return CourierData(
            login=data["login"],
            password=data["password"],
            first_name=data["firstName"]  # Преобразуем firstName в first_name
        )
    return None