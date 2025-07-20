import pytest
from faker import Faker

class Random_data:
    def generate_random_email():
        fake = Faker()
        email = fake.email()
        return email

    def generate_random_password():
        fake = Faker()
        password = fake.password(length=10)
        return password

    def generate_random_name():
        fake = Faker()
        name = fake.name()
        return name