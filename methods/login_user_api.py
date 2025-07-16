import requests
import allure
from urls.urls import Urls

class LoginUserApi:
    @staticmethod
    @allure.step('Вызов метода авторизации')
    def post_login_user(email,password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(Urls.URL_LOGIN_USER,json=payload)
        return response