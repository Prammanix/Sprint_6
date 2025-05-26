import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.data_generator import generate_name, generate_surname, generate_phone
from utils.urls import BASE_URL

@allure.feature("Order")
class TestOrder:
    @allure.title("Оформление заказа через кнопку '{order_button}' с цветом '{color}'")
    @pytest.mark.parametrize("order_button, color", [
        ("header", "black"),
        ("middle", "grey"),
    ])
    def test_order_scooter(self, driver, order_button, color):
        main = MainPage(driver)
        main.open(BASE_URL)
        if order_button == "header":
            main.click_order_header()
        else:
            main.click_order_middle()

        order = OrderPage(driver)
        name = generate_name()
        surname = generate_surname()
        phone = generate_phone()
        order.fill_personal_data(name, surname, "Новая площадь 3", phone)
        order.select_metro()
        order.click_next()
        order.select_date()
        order.select_rent_duration()
        if color == "black":
            order.select_color_black()
        else:
            order.select_color_grey()
        order.submit_order()
        order.confirm_order()
        order_number_text = order.get_order_number_text()
        assert "Номер заказа:" in order_number_text
