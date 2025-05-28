from faker import Faker
import random

fake = Faker('ru_RU')

def generate_name():
    return fake.first_name()

def generate_surname():
    return fake.last_name()

def generate_phone():
    return '+7' + ''.join([str(random.randint(0, 9)) for _ in range(10)])
