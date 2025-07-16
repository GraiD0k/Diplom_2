import allure
from methods.base_api import BaseApi
from methods.get_order_api import GetOrderApi

class TestGetOrder:
    @allure.title('Получение заказов конкретного пользователя - авторизованный пользователь')
    def test_get_order_with_authorization(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response_create_user = BaseApi.post_create_login(email,password,name)
        token = response_create_user.json()['accessToken']
        response = GetOrderApi.get_order(token)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Получение заказов конкретного пользователя - неавторизованный пользователь')
    def test_get_order_no_authorization(self):
        response = GetOrderApi.get_order()
        assert response.status_code == 401 and response.json()['success'] == False