import allure
from .base_page import BasePage
from .locators import OrderPageLocators
&nbsp;
&nbsp;

class OrderPage(BasePage):
    @allure.step("Заполнение личных данных: Имя, Фамилия, Адрес, Телефон")
    def fill_personal_data(self, name, surname, address, phone):
        self.input(OrderPageLocators.NAME_INPUT, name)
        self.input(OrderPageLocators.SURNAME_INPUT, surname)
        self.input(OrderPageLocators.ADDRESS_INPUT, address)
        self.input(OrderPageLocators.PHONE_INPUT, phone)
&nbsp;
&nbsp;

    @allure.step("Выбор станции метро")
    def select_metro(self):
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_OPTION_9)
&nbsp;
&nbsp;

    @allure.step("Клик по кнопке 'Далее'")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)
&nbsp;
&nbsp;

    @allure.step("Выбор даты")
    def select_date(self):
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_PICKER_DAY)
&nbsp;
&nbsp;

    @allure.step("Выбор срока аренды")
    def select_rent_duration(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION_1)
&nbsp;
&nbsp;

    @allure.step("Выбор цвета черного")
    def select_color_black(self):
        self.click(OrderPageLocators.COLOR_BLACK)
&nbsp;
&nbsp;

    @allure.step("Выбор цвета серого")
    def select_color_grey(self):
        self.click(OrderPageLocators.COLOR_GREY)
&nbsp;
&nbsp;

    @allure.step("Отправка заказа")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_SUBMIT)
&nbsp;
&nbsp;

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES)
&nbsp;
&nbsp;

    @allure.step("Получение текста номера заказа")
    def get_order_number_text(self):
        return self.find(OrderPageLocators.ORDER_NUMBER).text
&nbsp;
&nbsp;

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(OrderPageLocators.CLOSE_MODAL)