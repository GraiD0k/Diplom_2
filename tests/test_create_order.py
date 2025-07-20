import allure
from methods.base_api import BaseApi
from methods.create_order_api import CreateOrderApi

class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self,create_login):
        user_data = create_login
        token = user_data['token']
        response_create_order = CreateOrderApi.post_create_order(token,'Yes')
        assert response_create_order.status_code == 200 and response_create_order.json()['success']==True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_not_authorization(self):
        response_create_order = CreateOrderApi.post_create_order(ingredients='Yes')
        assert response_create_order.status_code == 200 and response_create_order.json()['success']==True

    @allure.title('Создание заказа с ингридиентами')
    def test_create_order_with_authorization_and_ingridients(self,create_login):
        user_data = create_login
        token = user_data['token']
        response_create_order = CreateOrderApi.post_create_order(token,'Yes')
        assert response_create_order.status_code == 200 and response_create_order.json()['success']==True


    @allure.title('Создание заказа без ингридиентов')
    def test_create_order_with_authorization_and_no_ingridients(self,create_login):
        user_data = create_login
        token = user_data['token']
        response_create_order = CreateOrderApi.post_create_order(token)
        assert response_create_order.status_code == 400 and response_create_order.json() == {'success': False,'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_authorization_and_error_ingridients(self,create_login):
        user_data = create_login
        token = user_data['token']
        response_create_order = CreateOrderApi.post_create_order(token,'Error')
        assert  response_create_order.status_code == 500
