import pytest
import allure
import requests
from config import URLs
from data.order_data import generate_order_data

@allure.suite("Тесты на создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [
        pytest.param(["BLACK"], id="BLACK"),
        pytest.param(["GREY"], id="GREY"),
        pytest.param(["BLACK", "GREY"], id="BLACK+GREY"),
        pytest.param([], id="No color")
    ])
    def test_create_order_with_different_colors(self, color):
        order_data = generate_order_data(color=color)
        response = requests.post(URLs.ORDERS, json=order_data)

        assert response.status_code == 201, "Неверный статус код"
        assert "track" in response.json(), "Отсутствует track-номер"

        with allure.step("Проверить что track-номер валидный"):
            track = response.json()["track"]
            assert isinstance(track, int) and track > 0, "Некорректный track-номер"