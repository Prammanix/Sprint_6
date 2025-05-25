from .base_page import BasePage
from .locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_personal_data(self, name, surname, address, phone):
        self.input(OrderPageLocators.NAME_INPUT, name)
        self.input(OrderPageLocators.SURNAME_INPUT, surname)
        self.input(OrderPageLocators.ADDRESS_INPUT, address)
        self.input(OrderPageLocators.PHONE_INPUT, phone)

    def select_metro(self):
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.METRO_OPTION_9)

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    def select_date(self):
        self.click(OrderPageLocators.DATE_INPUT)
        self.click(OrderPageLocators.DATE_PICKER_DAY)

    def select_rent_duration(self):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION_1)

    def select_color_black(self):
        self.click(OrderPageLocators.COLOR_BLACK)

    def select_color_grey(self):
        self.click(OrderPageLocators.COLOR_GREY)

    def submit_order(self):
        self.click(OrderPageLocators.ORDER_SUBMIT)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES)

    def get_order_number_text(self):
        return self.find(OrderPageLocators.ORDER_NUMBER).text

    def close_modal(self):
        self.click(OrderPageLocators.CLOSE_MODAL)
