import allure
from methods.base_api import BaseApi
from methods.get_order_api import GetOrderApi

class TestGetOrder:
    @allure.title('Получение заказов конкретного пользователя - авторизованный пользователь')
    def test_get_order_with_authorization(self,create_login):
        user_data = create_login
        token = user_data['token']
        response = GetOrderApi.get_order(token)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Получение заказов конкретного пользователя - неавторизованный пользователь')
    def test_get_order_no_authorization(self):
        response = GetOrderApi.get_order()
        assert response.status_code == 401 and response.json()['success'] is False