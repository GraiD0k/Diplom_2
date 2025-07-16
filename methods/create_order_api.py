import requests
import allure
from urls.urls import Urls

class CreateOrderApi:
    @staticmethod
    @allure.step('Вызов метода создания заказа')
    def post_create_order(token=None,ingredients='No'):
        if ingredients == 'Yes':
            payload = {
                "ingredients": ["61c0c5a71567675daaa70"]
            }
        elif ingredients=='Error':
            payload = {
                "ingredients": ["Test76"]
            }
        else:
            payload = {
            }
        header = {"Authorization": token}
        response = requests.post(Urls.URL_CREATE_ORDER,json=payload,headers=header,verify=False)
        return response