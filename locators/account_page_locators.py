from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGOUT_BUTTON = [
        By.XPATH,
        '//button[text()="Выход"]',
    ]  # Кнопка Выход в Личном Кабинете
    NAME_FIELD = [
        By.XPATH,
        '//input[@type="text"][@name="Name"]',
    ]  # Поле Имя в Личном Кабинете
    LOGIN_FIELD = [
        By.XPATH,
        '//input[@type="text"][@name="name"]',
    ]  # Поле Логин в Личном Кабинете
    ORDER_HISTORY = [
        By.XPATH,
        '//a[@href="/account/order-history"]',
    ]  # Кнопка История заказов в Личном Кабинете
