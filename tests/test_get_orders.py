import allure
import requests
from config import URLs

@allure.suite("Тесты на получение списка заказов")
class TestGetOrders:
    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        with allure.step("Отправить запрос на получение заказов"):
            response = requests.get(URLs.ORDERS)

        assert response.status_code == 200, "Неверный статус код"

        with allure.step("Проверить структуру ответа"):
            response_data = response.json()
            assert "orders" in response_data, "Отсутствует ключ 'orders'"
            assert isinstance(response_data["orders"], list), "orders не является списком"

            if len(response_data["orders"]) > 0:
                sample_order = response_data["orders"][0]
                assert "id" in sample_order, "У заказа отсутствует id"