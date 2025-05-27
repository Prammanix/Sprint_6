import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.data_generator import generate_name, generate_surname, generate_phone
from utils.test_data import FAQ_DATA
from pages.urls import BASE_URL
&nbsp;
&nbsp;

@allure.feature("Order")
class TestOrder:
    @allure.title("Оформление заказа через кнопку '{order_button}'")
    @pytest.mark.parametrize("order_button", ["header", "middle"])
    def test_order_scooter(self, driver, order_button):
        main = MainPage(driver)
        main.open(BASE_URL)
&nbsp;
&nbsp;

        # Клик по кнопке заказа в зависимости от параметра
        order_button_method = main.click_order_header if order_button == "header" else main.click_order_middle
        order_button_method()
&nbsp;
&nbsp;

        order = OrderPage(driver)
        name = generate_name()
        surname = generate_surname()
        phone = generate_phone()
        order.fill_personal_data(name, surname, "Новая площадь 3", phone)
        order.select_metro()
        order.click_next()
        order.select_date()
        order.select_rent_duration()
&nbsp;
&nbsp;

        # Выбор цвета в зависимости от параметра
        color_method = order.select_color_black if order_button == "header" else order.select_color_grey
        color_method()
&nbsp;
&nbsp;

        order.submit_order()
        order.confirm_order()
        order_number_text = order.get_order_number_text()
        assert "Номер заказа:" in order_number_text