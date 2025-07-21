from collections import namedtuple
import requests
import random
import string
from config import URLs

CourierData = namedtuple('CourierData', ['login', 'password', 'first_name'])

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def register_new_courier_and_return_login_password():
    data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

    response = requests.post(URLs.COURIER, data=data)
    if response.status_code == 201:
        return CourierData(
            login=data["login"],
            password=data["password"],
            first_name=data["firstName"]
        )
    return None