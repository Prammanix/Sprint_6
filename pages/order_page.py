import allure
from .base_page import BasePage
from .locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнение личных данных: {name} {surname}, {address}, {phone}")
    def fill_personal_data(self, name, surname, address, phone):
        self.input(OrderPageLocators.NAME_INPUT, name)
        self.input(OrderPageLocators.SURNAME_INPUT, surname)
        self.input(OrderPageLocators.ADDRESS_INPUT, address)
        self.input(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Выбор станции метро")
    def select_metro(self):
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_OPTION)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор даты доставки")
    def select_date(self):
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_PICKER_DAY)

    @allure.step("Выбор срока аренды")
    def select_rent_duration(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION_1)

    @allure.step("Выбор цвета: черный")
    def select_color_black(self):
        self.click(OrderPageLocators.COLOR_BLACK)

    @allure.step("Выбор цвета: серый")
    def select_color_grey(self):
        self.click(OrderPageLocators.COLOR_GREY)

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_SUBMIT)

    @allure.step("Подтверждение окна 'Да'")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES)

    @allure.step("Получение номера заказа")
    def get_order_number_text(self):
        return self.find(OrderPageLocators.ORDER_NUMBER).text

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(OrderPageLocators.CLOSE_MODAL)
