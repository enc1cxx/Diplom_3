from locators.orders_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_newer_order(self):
        with allure.step("Нажимаем на самый новый заказ"):
            self.push_element(OrderPageLocators.NEW_ORDER_IN_LINE)
