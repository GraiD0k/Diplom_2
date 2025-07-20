import pytest
from helpers.helpers import Random_data
from methods.base_api import BaseApi



@pytest.fixture
def create_login(login_data):
    name = login_data['name']
    password = login_data['password']
    email = login_data['email']
    response_create = BaseApi.post_create_login(email,password,name)
    token = response_create.json()['accessToken']
    yield {
        'name': name,
        'password': password,
        'email': email,
        'token': token,
        'response_create':response_create
    } # Можно добавить очистку после теста при необходимости
    response_delete = BaseApi.delete_login(token)
    assert response_delete.status_code == 202 and response_delete.json() == {'success': True,
                                                                                'message': 'User successfully removed'}
@pytest.fixture
def login_data():
    return {"name": Random_data.generate_random_name(),"password": Random_data.generate_random_password(),"email": Random_data.generate_random_email()}
