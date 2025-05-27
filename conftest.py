import pytest
from selenium import webdriver
&nbsp;
&nbsp;

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # убери если нужен видимый браузер
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()