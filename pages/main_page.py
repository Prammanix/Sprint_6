import allure
from .base_page import BasePage
from .locators import MainPageLocators
&nbsp;
&nbsp;

class MainPage(BasePage):
    @allure.step("Клик по вопросу FAQ с индексом: {index}")
    def click_faq_question(self, index):
        self.click(MainPageLocators.FAQ_QUESTIONS[index])
&nbsp;
&nbsp;

    @allure.step("Получение текста ответа FAQ с индексом: {index}")
    def get_faq_answer_text(self, index):
        return self.find(MainPageLocators.FAQ_ANSWERS[index]).text
&nbsp;
&nbsp;

    @allure.step("Клик по кнопке 'Заказать' в заголовке")
    def click_order_header(self):
        self.click(MainPageLocators.ORDER_BUTTON_HEADER)
&nbsp;
&nbsp;

    @allure.step("Клик по кнопке 'Заказать' в середине страницы")
    def click_order_middle(self):
        self.click(MainPageLocators.ORDER_BUTTON_MIDDLE)