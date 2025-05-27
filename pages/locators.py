from selenium.webdriver.common.by import By
&nbsp;
&nbsp;

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
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, ".Header_Nav__AGCXC > button:nth-child(1)")
    ORDER_BUTTON_MIDDLE = (By.CSS_SELECTOR, ".Button_UltraBig__UU3Lp")
&nbsp;
&nbsp;

class OrderPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, ".Order_Form__17u6u > div:nth-child(1) > input:nth-child(1)")
    SURNAME_INPUT = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(2) > input:nth-child(1)")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(3) > input:nth-child(1)")
    METRO_INPUT = (By.CSS_SELECTOR, ".select-search__input")
    METRO_OPTION_9 = (By.CSS_SELECTOR, "li.select-search__row:nth-child(9)")
    PHONE_INPUT = (By.CSS_SELECTOR, "div.Input_InputContainer__3NykH:nth-child(5) > input:nth-child(1)")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")
    DATE_INPUT = (By.CSS_SELECTOR, ".react-datepicker-ignore-onclickoutside")
    DATE_PICKER_DAY = (By.CSS_SELECTOR, ".react-datepicker__day--031")
    RENT_DROPDOWN = (By.CSS_SELECTOR, ".Dropdown-control")
    RENT_OPTION_1 = (By.CSS_SELECTOR, "div.Dropdown-menu > div:nth-child(1)")
    COLOR_BLACK = (By.CSS_SELECTOR, "label[for='black']")
    COLOR_GREY = (By.CSS_SELECTOR, "label[for='grey']")
    ORDER_SUBMIT = (By.CSS_SELECTOR, ".Button_Middle__1CSJM:nth-child(2)")
    CONFIRM_YES = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.Order_Text__2broi")
    CLOSE_MODAL = (By.CSS_SELECTOR, "button:contains('Посмотреть статус')")