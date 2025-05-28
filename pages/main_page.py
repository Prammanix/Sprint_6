import allure
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index):
        self.click(MainPageLocators.FAQ_QUESTIONS[index])

    @allure.step("Получение текста ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        return self.find(MainPageLocators.FAQ_ANSWERS[index]).text

    @allure.step("Клик по кнопке заказа (локатор: {locator})")
    def click_order_button(self, locator):
        self.click(locator)
