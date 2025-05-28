import pytest
import allure
from pages.main_page import MainPage
from utils.test_data import FAQ_DATA
from pages.urls import BASE_URL

@allure.feature("FAQ")
class TestFAQ:
    @allure.title("Проверка отображения ответа на вопрос FAQ: {expected_question}")
    @pytest.mark.parametrize("index,expected_question,expected_answer", [
        (i, FAQ_DATA[i][0], FAQ_DATA[i][1]) for i in range(len(FAQ_DATA))
    ])
    def test_faq_question(self, driver, index, expected_question, expected_answer):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.click_faq_question(index)
        answer = page.get_faq_answer_text(index)
        assert expected_answer in answer
