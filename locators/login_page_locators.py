from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = [
        By.XPATH,
        '//label[text()="Email"]/following-sibling::input',
    ]  # Поле ввода Email на форме Вход
    PASSWORD_FIELD = [
        By.XPATH,
        '//label[text()="Пароль"]/following-sibling::input',
    ]  # Поле ввода Пароль на форме Вход
    ENTER_BUTTON = [
        By.XPATH,
        '//button[text()="Войти"]',
    ]  # Кнопка Войти в аккаунт на форме Вход
    RESTORE_PASSWORD_LINK = [
        By.XPATH,
        '//a[@href="/forgot-password"]',
    ]  # Ссылка Восстановить пароль на форме Вход
    REGISTRATION_LINK = [
        By.XPATH,
        '//a[@href="/register"]',
    ]  # Ссылка с предложением Зарегистрироваться на форме Вход
    RESTORE_PASSWORD_HEADER = [
        By.XPATH,
        '//h2[text()="Восстановление пароля"]',
    ]  # Заголовок страницы "Восстановление пароля"
    INPUT_CODE_LABEL = [
        By.XPATH,
        '//label[text()="Введите код из письма"]',
    ]  # Плейсхолдер страницы "Введите код из письма"
    INPUT_EMAIL_INPUT = [
        By.XPATH,
        '//input[@name="name"]',
    ]  # Поле ввода емейла для восстановления пароля
    RESTORE_PASSWORD_BUTTON = [
        By.XPATH,
        '//button[text()="Восстановить"]',
    ]  # Кнопка "Восстановить"
    HIDE_SHOW_BUTTON = [By.CLASS_NAME, "input__icon"]  # Кнопка "Показать/скрыть пароль"
    PASSWORD_CONTAINER = [
        By.XPATH,
        '//label[text()="Пароль"]/parent::div',
    ]  # Контейнер поля ввода Пароль на форме Вход
