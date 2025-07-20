import allure
from methods.login_user_api import LoginUserApi
from data.login_user_data import LoginUserData

class TestLoginUser:
    @allure.title('логин под существующим пользователем')
    def test_login_user(self,create_login):
        user_data = create_login

        response = LoginUserApi.post_login_user(user_data ['email'], user_data['password'])
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('логин с неверным логином и паролем')
    def test_login_user_exist_email_and_password(self):
        response = LoginUserApi.post_login_user('error','error')
        assert response.status_code == 401 and response.json()['message'] == LoginUserData.TEXT_LOGIN_ERROR