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
        response = requests.post(Urls.URL_CREATE_USER,json=payload,verify=False)
        return response

    @staticmethod
    @allure.step('Вызываем метод удаления пользователя')
    def delete_login(delete_token):
        header = {"Authorization": delete_token}
        response = requests.delete(Urls.URL_CHANGE_USER,headers=header,verify=False)
        return response