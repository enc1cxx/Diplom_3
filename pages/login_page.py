from locators.login_page_locators import LoginPageLocators
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_restore_password(self):
        with allure.step("Переходим в восстановление пароля"):
            self.push_element(LoginPageLocators.RESTORE_PASSWORD_LINK)
            self.wait_visibility(LoginPageLocators.RESTORE_PASSWORD_HEADER)

    def login(self, email, password):
        """Входим в личный кабинет"""
        with allure.step(f"Входим в личный кабинет"):
            self.push_element(MainPageLocators.ACCOUNT_BUTTON)
            self.send_keys(LoginPageLocators.EMAIL_FIELD, email)
            self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
            self.push_element(LoginPageLocators.ENTER_BUTTON)
            self.wait_invisibility(LoginPageLocators.ENTER_BUTTON)
