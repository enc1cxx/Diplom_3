from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = [By.XPATH, '//a[@href="/account"]']  #'Кнопка "Личный Кабинет"
    CONSTRUCTOR_BUTTON = [By.XPATH, '//ul//a[@href="/"]']  # Кнопка "Конструктор"
    CONSTRUCTOR_HEADER = [
        By.XPATH,
        '//h1[text()="Соберите бургер"]',
    ]  # Заголовок раздела "Конструктор"
    ORDER_FEED_BUTTON = [By.XPATH, '//ul//a[@href="/feed"]']  # Кнопка "Лента заказов"
    ORDER_FEED_HEADER = [
        By.XPATH,
        '//h1[text()="Лента заказов"]',
    ]  #'Заголовок раздела "Лента заказов"
    STELLAR_BURGERS_LOGO = [By.XPATH, '//div/a[@href="/"]']  # Логотип "Stellar Burgers"
    LOGIN_BUTTON = [
        By.XPATH,
        '//button[text()="Войти в аккаунт"]',
    ]  # Кнопка "Войти в аккаунт" на главной странице
