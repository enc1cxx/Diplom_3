import allure
from constants.links import Links
from locators.login_page_locators import LoginPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.epic("Stellar Burger")
@allure.feature("Проверки восстановления пароля")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Алексей Александров")
class TestRestorePassword:

    @allure.title(
        "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    @allure.description(
        "Проверяем, что произошел переход на страницу восстановления пароля по кнопке «Восстановить "
        "пароль»"
    )
    def test_follow_to_restore_password(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_login_form()
        account_page = AccountPage(driver)
        login_page.go_to_restore_password()
        with allure.step(
            "Проверяем, что произошел переход на страницу восстановления пароля по кнопке «Восстановить "
            "пароль»"
        ):
            assert (
                account_page.is_displayed(LoginPageLocators.RESTORE_PASSWORD_HEADER)
                and account_page.get_current_url() == Links.FORGOT_PASSWORD
            )

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    @allure.description(
        "Проверяем, что произошел переход на страницу ввода кода из письма"
    )
    def test_follow_to_reset_password(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_login_form()
        login_page.go_to_restore_password()
        login_page.fill_email_to_restore_pass(create_and_delete_user["email"])
        login_page.push_restore_pass()
        with allure.step(
            "Проверяем, что произошел переход на страницу ввода кода из письма"
        ):
            assert (
                login_page.is_displayed(LoginPageLocators.INPUT_CODE_LABEL)
                and login_page.get_current_url() == Links.RESET_PASSWORD
            )

    @allure.title("Клик по кнопке показать/скрыть пароль")
    @allure.description(
        "Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"
    )
    def test_reset_password_field_flash(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.go_to_login_form()
        login_page.go_to_restore_password()
        login_page.fill_email_to_restore_pass(create_and_delete_user["email"])
        login_page.push_restore_pass()
        with allure.step(
            "Проверяем, что у контейнера поля ввода 'Пароль' отсутствует подсветка"
        ):
            assert "input_status_active" not in login_page.get_element_attribute(
                LoginPageLocators.PASSWORD_CONTAINER, "class"
            )
        login_page.click_show_hide_pass()
        with allure.step(
            "Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"
        ):
            assert "input_status_active" in login_page.get_element_attribute(
                LoginPageLocators.PASSWORD_CONTAINER, "class"
            )
