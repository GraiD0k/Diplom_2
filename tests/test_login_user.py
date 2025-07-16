import allure
from methods.base_api import BaseApi
from methods.login_user_api import LoginUserApi
from data.login_user_data import LoginUserData

class TestLoginUser:
    @allure.title('логин под существующим пользователем')
    def test_login_user(self,generate_random_email,generate_random_password,generate_random_name):
        email = generate_random_email
        password = generate_random_password
        name = generate_random_name
        respose_create_user = BaseApi.post_create_login(email,password,name)
        response = LoginUserApi.post_login_user(email,password)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('логин с неверным логином и паролем')
    def test_login_user_exist_email_and_password(self):
        response = LoginUserApi.post_login_user('error','error')
        assert response.status_code == 401 and response.json()['message'] == LoginUserData.TEXT_LOGIN_ERROR