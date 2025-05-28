import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.data_generator import generate_name, generate_surname, generate_phone
from pages.urls import BASE_URL
from pages.locators import MainPageLocators

@allure.feature("Order")
class TestOrder:
    @allure.title("Оформление заказа через кнопку")
    @pytest.mark.parametrize("order_button_locator, color_key", [
        (MainPageLocators.ORDER_BUTTON_HEADER, "header"),
        (MainPageLocators.ORDER_BUTTON_MIDDLE, "middle")
    ])
    def test_order_scooter(self, driver, order_button_locator, color_key):
        main = MainPage(driver)
        main.open(BASE_URL)
        main.click_order_button(order_button_locator)

        order = OrderPage(driver)
        name = generate_name()
        surname = generate_surname()
        phone = generate_phone()
        order.fill_personal_data(name, surname, "Новая площадь 3", phone)
        order.select_metro()
        order.click_next()
        order.select_date()
        order.select_rent_duration()
        order.select_color(color_key)
        order.submit_order()
        order.confirm_order()
        order_number_text = order.get_order_number_text()
        assert "Номер заказа:" in order_number_text
