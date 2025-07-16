import requests
import allure
from urls.urls import Urls

class GetOrderApi:
    @staticmethod
    @allure.step('Вызов метода получения заказы конкретного пользователя')
    def get_order(token=None):
        header = {"Authorization": token}
        response = requests.get(Urls.URL_GET_ORDER,headers=header)
        return response