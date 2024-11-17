from selenium.webdriver.common.by import By


class OrderPageLocators:
    NEW_ORDER_IN_LINE = [
        By.XPATH,
        '//ul[@class="OrderFeed_list__OLh59"]/li[1]/a',
    ]  # Карточка самого нового заказа
    STRUCTURE_HEADER = [
        By.XPATH,
        '//ul[@class="OrderFeed_list__OLh59"]/li[1]',
    ]  # Заголовок с составом на карточке заказа
    NUMBER_OF_ORDER = [
        By.XPATH,
        '//ul//li[1]//p[@class="text text_type_digits-default"]',
    ]  # Номер  самого нового заказа
    ALL_TIME_COUNT = [
        By.XPATH,
        '//div[@class]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]',
    ]  # Число заказов за все время
    TODAY_COUNT = [
        By.XPATH,
        '//div/div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]',
    ]  # Число заказов за сегодня
    ORDER_IN_PROGRESS = [
        By.XPATH,
        '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li',
    ]  # Заказ в работе
    ALL_ORDERS_DONE = [
        By.XPATH,
        '//li[@class="text text_type_main-small" and contains(text(), "Все текущие заказы готовы!")]',
    ]  # Лейбл "Все текущие заказы готовы!"
    ORDER_FEED_HEADER = [
        By.XPATH,
        '//h1[text()="Лента заказов"]',
    ]  #'Заголовок раздела "Лента заказов"
