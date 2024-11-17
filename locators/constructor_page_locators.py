from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    FILLINGS_TAB = [
        By.XPATH,
        '//span[text()="Начинки"]/parent::div',
    ]  # Вкладка с Начинками
    BUNS_TAB = [By.XPATH, '//span[text()="Булки"]/parent::div']  # Вкладка с Булками
    SAUCES_TAB = [By.XPATH, '//span[text()="Соусы"]/parent::div']  # Вкладка с Соусами
    FLUO_BUN = [
        By.XPATH,
        '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]',
    ]  # Карточка "Флюоресцентная булка"
    INFO_ABOUT_INGREDIENT = [
        By.XPATH,
        '//h2[text()="Детали ингредиента"]',
    ]  # Заголовок окна "Детали ингредиента"
    CLOSE_INFO = [
        By.XPATH,
        '//button[@class="Modal_modal__close_modified__3V5XS '
        'Modal_modal__close__TnseK"]',
    ]  # Кнопка закрыть "Детали ингредиента"
    BURGER_CONSTRUCTOR = [
        By.XPATH,
        '//ul[@class="BurgerConstructor_basket__list__l9dp_"]',
    ]  # Конструктор бургеров
    FLUO_BUN_COUNTER = [
        By.XPATH,
        '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p['
        '@class="counter_counter__num__3nue1"]',
    ]  # Счетчик Флюоресцентных булкок
    CREATE_ORDER_BUTTON = [
        By.XPATH,
        '//button[text()="Оформить заказ"]',
    ]  # Кнопка "Оформить заказ"
    CREATE_ID_HEADER = [
        By.XPATH,
        '//p[text()="идентификатор заказа"]',
    ]  # Заголовок "Идентификатор заказа"
    NUMBER_OF_ORDER = [
        By.XPATH,
        '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text '
        'text_type_digits-large mb-8"]',
    ]  # Поле "Номер заказа"
    MODAL = [By.CLASS_NAME, "div.Modal_modal_opened__3ISw4"]  # Модалка
