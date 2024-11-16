from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.orders_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_order_feed(self):
        with allure.step("Переходим в ленту заказов"):
            self.push_element(MainPageLocators.ORDER_FEED_BUTTON)
            self.wait_visibility(OrderPageLocators.ALL_TIME_COUNT)

    def go_to_constructor(self):
        with allure.step("Переходим в конструктор"):
            self.push_element(MainPageLocators.CONSTRUCTOR_BUTTON)
            self.wait_visibility(MainPageLocators.CONSTRUCTOR_HEADER)

    def go_to_account(self):
        with allure.step("Переходим в личный кабинет"):
            self.push_element(MainPageLocators.ACCOUNT_BUTTON)
            self.wait_visibility(AccountPageLocators.NAME_FIELD)

    def go_to_login_form(self):
        with allure.step("Переходим на форму авторизации"):
            self.push_element(MainPageLocators.ACCOUNT_BUTTON)
            self.wait_visibility(LoginPageLocators.ENTER_BUTTON)
