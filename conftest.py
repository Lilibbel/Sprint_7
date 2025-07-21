import pytest
from api.courier_api import CourierApi
from data.courier_data import register_new_courier_and_return_login_password

@pytest.fixture
def create_and_delete_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    # Удаление после теста
    if courier_data:
        login_response = CourierApi.login(courier_data.login, courier_data.password)
        if login_response.status_code == 200:
            CourierApi.delete(login_response.json()["id"])