import allure
from methods.base_api import BaseApi
from data.create_user_data import CreateUserData

class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = BaseApi.post_create_login(email,password,name)
        with allure.step('Проверяем код и текст ответа'):
            assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_create_exist_user_error(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        response = BaseApi.post_create_login(email,password,name)
        response_error = BaseApi.post_create_login(email,password,name)
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code == 403 and response_error.json()['message'] ==CreateUserData.TEXT_CREATE_USER_403

    @allure.title('Создание пользователя, не передавая пароль')
    def test_create_user_no_password_error(self,generate_random_email,generate_random_name):
        email = generate_random_email
        name = generate_random_name
        response = BaseApi.post_create_login(email,'',name)
        response_error = BaseApi.post_create_login(email,'',name)
        with allure.step('Проверяем код и текст ответа'):
            assert response_error.status_code == 403 and response_error.json()['message'] ==CreateUserData.TEXT_CREATE_USER_NO_PASSWORD