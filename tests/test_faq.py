import pytest
import allure
from pages.main_page import MainPage
from utils.test_data import FAQ_DATA
&nbsp;
&nbsp;

@allure.feature("FAQ")
class TestFAQ:
    @allure.title("Проверка вопросов FAQ")
    @pytest.mark.parametrize("index,expected_question,expected_answer", [
        (i, FAQ_DATA[i][0], FAQ_DATA[i][1]) for i in range(len(FAQ_DATA))
    ])
    def test_faq_question(self, driver, index, expected_question, expected_answer):
        page = MainPage(driver)
        page.open("https://qa-scooter.praktikum-services.ru/")
        page.click_faq_question(index)
        answer = page.get_faq_answer_text(index)
        assert expected_answer in answer