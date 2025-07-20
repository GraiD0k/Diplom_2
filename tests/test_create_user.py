import allure
from methods.base_api import BaseApi
from data.create_user_data import CreateUserData

class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self,create_login):
        user_data = create_login
        response = user_data['response_create']
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_create_exist_user_error(self,create_login):
        user_data = create_login
        response_error = BaseApi.post_create_login(user_data['email'],user_data['password'],user_data['name'])
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code == 403 and response_error.json()['message'] == CreateUserData.TEXT_CREATE_USER_403

    @allure.title('Создание пользователя, не передавая пароль')
    def test_create_user_no_password_error(self,login_data):
        email = login_data
        name = login_data
        response_error = BaseApi.post_create_login(email,'',name)
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code == 403 and response_error.json()['message'] ==CreateUserData.TEXT_CREATE_USER_NO_PASSWORD
