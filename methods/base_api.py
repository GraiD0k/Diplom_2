import requests
import allure
from urls.urls import Urls

class BaseApi:
    @staticmethod
    @allure.step('Вызываем метод создания пользователя')
    def post_create_login(email,password,name):
        payload = {
    "email": email,
    "password": password,
    "name":name
}
        response = requests.post(Urls.URL_CREATE_USER,json=payload)
        return response