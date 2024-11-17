from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_order_feed(self):
        with allure.step("Переходим в ленту заказов"):
            self.push_element(MainPageLocators.ORDER_FEED_BUTTON)

    def go_to_constructor(self):
        with allure.step("Переходим в конструктор"):
            self.push_element(MainPageLocators.CONSTRUCTOR_BUTTON)
            self.wait_visibility(MainPageLocators.CONSTRUCTOR_HEADER)

    def go_to_account(self):
        with allure.step("Переходим в личный кабинет"):
            self.push_element(MainPageLocators.ACCOUNT_BUTTON)

    def go_to_login_form(self):
        with allure.step("Переходим на форму авторизации"):
            self.push_element(MainPageLocators.ACCOUNT_BUTTON)
