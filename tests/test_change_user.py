import allure
from methods.base_api import BaseApi
from methods.change_user_api import ChangeUserApi

class TestChangeUser:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = BaseApi.post_create_login(email,password,name)
        token = response.json()['accessToken']
        new_email = generate_random_email
        new_password = generate_random_password
        response_change_user = ChangeUserApi.patch_change_user(new_email,new_password,token)
        assert response_change_user.status_code == 200 and response_change_user.json()['success']==True

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_user_no_authorization_error(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = BaseApi.post_create_login(email,password,name)
        new_email = generate_random_email
        new_password = generate_random_password
        response_change_user = ChangeUserApi.patch_change_user(new_email,new_password,'')
        assert response_change_user.status_code == 401 and response_change_user.json()['success']==False