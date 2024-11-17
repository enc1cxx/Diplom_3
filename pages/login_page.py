from locators.login_page_locators import LoginPageLocators
import allure
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
            self.send_keys(LoginPageLocators.EMAIL_FIELD, email)
            self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
            self.push_element(LoginPageLocators.ENTER_BUTTON)
            self.wait_invisibility(LoginPageLocators.ENTER_BUTTON)

    def fill_email_to_restore_pass(self, email):
        with allure.step("Вводим в поле ввода Емейла почту пользователя"):
            self.send_keys(LoginPageLocators.INPUT_EMAIL_INPUT, email)

    def push_restore_pass(self):
        with allure.step("Нажимаем кнопку Восстановить"):
            self.push_element(LoginPageLocators.RESTORE_PASSWORD_BUTTON)
            self.wait_visibility(LoginPageLocators.INPUT_CODE_LABEL)

    def click_show_hide_pass(self):
        with allure.step("Нажимаем на кнопку показать/скрыть пароль"):
            self.click_element(LoginPageLocators.HIDE_SHOW_BUTTON)