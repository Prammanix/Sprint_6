import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента с локатором: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов с локатором: {locator}")
    def finds(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу с локатором: {locator}")
    def click(self, locator):
        self.find(locator).click()

    @allure.step("Ввод значения '{value}' в элемент с локатором: {locator}")
    def input(self, locator, value):
        el = self.find(locator)
        el.clear()
        el.send_keys(value)
