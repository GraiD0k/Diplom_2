import allure
from methods.base_api import BaseApi
from methods.change_user_api import ChangeUserApi
from helpers.helpers import Random_data

class TestChangeUser:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_user(self,create_login):
        user_data = create_login
        token = user_data['token']
        new_email = Random_data.generate_random_email()
        new_password = Random_data.generate_random_password()
        response_change_user = ChangeUserApi.patch_change_user(
            email=new_email,
            password=new_password,
            token=token
        )
        assert response_change_user.status_code == 200 and response_change_user.json()['success'] is True

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_user_no_authorization_error(self,create_login):
        user_data = create_login
        new_email = Random_data.generate_random_email()
        new_password = Random_data.generate_random_password()
        response_change_user = ChangeUserApi.patch_change_user(new_email,new_password,'')
        assert response_change_user.status_code == 401 and response_change_user.json()['success'] is False
