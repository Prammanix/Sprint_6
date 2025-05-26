import allure
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    FAQ_QUESTIONS = MainPageLocators.FAQ_QUESTIONS
    FAQ_ANSWERS = MainPageLocators.FAQ_ANSWERS
    ORDER_BUTTON_HEADER = MainPageLocators.ORDER_BUTTON_HEADER
    ORDER_BUTTON_MIDDLE = MainPageLocators.ORDER_BUTTON_MIDDLE

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_faq_question(self, index):
        self.click(self.FAQ_QUESTIONS[index])

    @allure.step("Получение текста ответа FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        return self.find(self.FAQ_ANSWERS[index]).text

    @allure.step("Клик по кнопке 'Заказать' в хедере")
    def click_order_header(self):
        self.click(self.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке 'Заказать' в середине страницы")
    def click_order_middle(self):
        self.click(self.ORDER_BUTTON_MIDDLE)
