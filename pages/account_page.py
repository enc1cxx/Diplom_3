from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure
from selenium.webdriver import Keys
from locators.account_page_locators import AccountPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
            self.wait_visibility(LoginPageLocators.EMAIL_FIELD)

    def go_to_restore_password(self):
        with allure.step("Переходим в восстановление пароля"):
            self.push_element(LoginPageLocators.RESTORE_PASSWORD_LINK)
            self.wait_visibility(LoginPageLocators.RESTORE_PASSWORD_HEADER)
