import pytest
import requests

class TestCreateOrder:
    base_url = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    # Параметризация: 4 варианта цвета (BLACK, GREY, оба, без цвета)
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_different_colors(self, color):
        payload = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2025-07-20",
            "comment": "Тестовый заказ",
            "color": color
        }

        response = requests.post(self.base_url, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()