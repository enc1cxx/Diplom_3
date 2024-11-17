from locators.orders_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_newer_order(self):
        with allure.step("Нажимаем на самый новый заказ"):
            self.push_element(OrderPageLocators.NEW_ORDER_IN_LINE)

    def wait_load_order_page(self):
        with allure.step("Дожидаемся загрузки страницы Лента заказов"):
            self.wait_visibility(OrderPageLocators.ALL_TIME_COUNT)

    def wait_not_all_orders_done(self):
        with allure.step("Дожидаемся отсутствия надписи Все заказы готовы"):
            self.wait_invisibility(OrderPageLocators.ALL_ORDERS_DONE)

    def get_today_count(self):
        return self.text_in_element(OrderPageLocators.TODAY_COUNT)

    def get_all_time_count(self):
        return self.text_in_element(OrderPageLocators.ALL_TIME_COUNT)

    def get_order_in_progress(self):
        return self.text_in_element(OrderPageLocators.ORDER_IN_PROGRESS)
