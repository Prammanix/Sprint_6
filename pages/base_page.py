import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Ввод значения '{value}' в элемент: {locator}")
    def input(self, locator, value):
        el = self.find(locator)
        el.clear()
        el.send_keys(value)
