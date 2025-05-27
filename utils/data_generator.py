from faker import Faker
import random
&nbsp;
&nbsp;

fake = Faker('ru_RU')
&nbsp;
&nbsp;

def generate_name():
    return fake.first_name()
&nbsp;
&nbsp;

def generate_surname():
    return fake.last_name()
&nbsp;
&nbsp;

def generate_phone():
    return '+7' + ''.join([str(random.randint(0, 9)) for _ in range(10)])