import pytest
import requests
from data.courier_data import register_new_courier_and_return_login_password

class TestCreateCourier:
    base_url = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    # 1. Успешное создание курьера
    def test_create_courier_success(self):
        courier_data = register_new_courier_and_return_login_password()
        assert len(courier_data) == 3  # Проверяем, что вернулся логин, пароль и имя

    # 2. Нельзя создать двух одинаковых курьеров
    def test_create_duplicate_courier_fails(self):
        courier_data = register_new_courier_and_return_login_password()
        login, password, first_name = courier_data

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(self.base_url, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    # 3. Обязательные поля (негативные тесты)
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_fails(self, missing_field):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }
        del payload[missing_field]  # Удаляем одно поле

        response = requests.post(self.base_url, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"