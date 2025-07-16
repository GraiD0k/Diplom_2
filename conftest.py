import pytest
from faker import Faker

@pytest.fixture()
def generate_random_email():
    fake = Faker()
    email = fake.email()
    return email

@pytest.fixture()
def generate_random_password():
    fake = Faker()
    password = fake.password(length=10)
    return password

@pytest.fixture()
def generate_random_name():
    fake = Faker()
    name = fake.name()
    return name