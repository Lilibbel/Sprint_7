import requests
from config import URLs


class CourierApi:
    @staticmethod
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(URLs.COURIER, data=payload)

    @staticmethod
    def login(login, password):
        payload = {"login": login, "password": password}
        return requests.post(URLs.LOGIN, data=payload)

    @staticmethod
    def delete(courier_id):
        return requests.delete(f"{URLs.COURIER}/{courier_id}")