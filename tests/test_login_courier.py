import pytest
import allure
from api.courier_api import CourierApi
from data.courier_data import register_new_courier_and_return_login_password
from config import URLs
import requests


@allure.suite("Тесты на авторизацию курьера")
class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        response = CourierApi.login(courier_data.login, courier_data.password)

        assert response.status_code == 200, "Неверный статус код"
        assert "id" in response.json(), "Отсутствует id в ответе"

        with allure.step("Проверить что id валидный"):
            assert isinstance(response.json()["id"], int), "id должен быть числом"

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password_fails(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        response = CourierApi.login(courier_data.login, "wrong_password")

        assert response.status_code == 404, "Неверный статус код"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация без обязательного поля: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_field_fails(self, missing_field):
        courier_data = register_new_courier_and_return_login_password()
        payload = {
            "login": courier_data.login,
            "password": courier_data.password
        }
        del payload[missing_field]

        response = requests.post(URLs.LOGIN, data=payload)
        assert response.status_code == 400, "Неверный статус код"
        assert response.json()["message"] == "Недостаточно данных для входа"