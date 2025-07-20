import pytest
import requests
from data.courier_data import register_new_courier_and_return_login_password

class TestLoginCourier:
    base_url = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"

    # 1. Успешная авторизация
    def test_login_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }

        response = requests.post(self.base_url, data=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    # 2. Неверный пароль → 404
    def test_login_wrong_password_fails(self):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": "wrong_password"
        }

        response = requests.post(self.base_url, data=payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    # 3. Нет обязательного поля → 400
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, missing_field):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        del payload[missing_field]

        response = requests.post(self.base_url, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"