from pages.base_page import BasePage
import allure
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_order_history(self):
        with allure.step("Переходим в историю заказов"):
            self.wait_visibility(AccountPageLocators.NAME_FIELD)
            self.push_element(AccountPageLocators.ORDER_HISTORY)

    def logout(self):
        with allure.step("Выходим из аккаунта"):
            self.push_element(AccountPageLocators.LOGOUT_BUTTON)
            self.wait_invisibility(AccountPageLocators.NAME_FIELD)

    def get_name(self):
        return self.get_element_attribute(AccountPageLocators.NAME_FIELD, "value")
    
    def get_login(self):
        return self.get_element_attribute(AccountPageLocators.LOGIN_FIELD, "value")
    
    def wait_load_account(self):
        with allure.step("Дожидаемся загрузки страницы Аккаунт"):
            self.wait_visibility(AccountPageLocators.NAME_FIELD)
