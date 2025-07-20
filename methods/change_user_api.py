import requests
import allure
from urls.urls import Urls

class ChangeUserApi:
    @staticmethod
    @allure.step('Вызов метода изменения данных пользователя')
    def patch_change_user(email,password,token):
        payload = {
            "email": email,
            "password": password
        }
        header = {"Authorization": token}
        response = requests.patch(Urls.URL_CHANGE_USER,json=payload,headers=header,verify=False)
        return response