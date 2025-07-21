import pytest
import allure
from api.courier_api import CourierApi
from data.courier_data import *

@allure.suite("Тесты на создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        response = CourierApi.create_courier(
            courier_data.login,
            courier_data.password,
            courier_data.first_name
        )

        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Попытка создания дубликата курьера")
    def test_create_duplicate_courier_fails(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        response = CourierApi.create_courier(
            courier_data.login,
            courier_data.password,
            courier_data.first_name
        )

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    @allure.title("Создание курьера без обязательного поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_fails(self, missing_field):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data.login,
            "password": courier_data.password,
            "firstName": courier_data.first_name
        }
        del payload[missing_field]

        response = requests.post(URLs.COURIER, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"