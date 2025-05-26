from selenium.webdriver.common.by import By

class MainPageLocators:

    FAQ_QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]
    FAQ_ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(text(),'Заказать') and ancestor::div[contains(@class,'Header')]]")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button")

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//li//button[contains(@class, 'select-search__option')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_DAY = (By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]/following-sibling::div[1]")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION_1 = (By.XPATH, "//div[@class='Dropdown-menu']/div[1]")
    COLOR_BLACK = (By.XPATH, "//label[@for='black']")
    COLOR_GREY = (By.XPATH, "//label[@for='grey']")
    ORDER_SUBMIT = (By.XPATH, "//button[contains(text(),'Заказать')]")
    CONFIRM_YES = (By.XPATH, "//button[contains(text(),'Да')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(text(),'Номер заказа')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")