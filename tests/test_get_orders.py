import requests

class TestGetOrders:
    base_url = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

    def test_get_orders_returns_list(self):
        response = requests.get(self.base_url)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)