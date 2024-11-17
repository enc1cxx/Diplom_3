import allure
from constants.links import Links
from locators.login_page_locators import LoginPageLocators
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.epic("Stellar Burger")
@allure.feature("Проверки личного кабинета")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Алексей Александров")
class TestAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description(
        "Проверяем, что в личном кабинете отображаются наши пользовательские данные"
    )
    def test_follow_to_account(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            create_and_delete_user["email"], create_and_delete_user["password"]
        )
        main_page.go_to_account()
        account_page = AccountPage(driver)
        account_page.wait_load_account()
        name = account_page.get_name()
        login = account_page.get_login()
        with allure.step(
            "Проверяем, что в личном кабинете отображаются наши пользовательские данные"
        ):
            assert (
                name == create_and_delete_user["name"]
                and login == create_and_delete_user["email"]
            )

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Проверяем, что произошел переход в историю заказов")
    def test_follow_to_order_history(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            create_and_delete_user["email"], create_and_delete_user["password"]
        )
        main_page.go_to_account()
        account_page = AccountPage(driver)
        account_page.wait_load_account()
        account_page.go_to_order_history()
        with allure.step("Проверяем, что произошел переход в историю заказов"):
            assert account_page.get_current_url() == Links.ORDER_HISTORY

    @allure.title("Выход из аккаунта")
    @allure.description("Проверяем, что произошел выход из аккаунта")
    def test_logout(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            create_and_delete_user["email"], create_and_delete_user["password"]
        )
        main_page.go_to_account()
        account_page = AccountPage(driver)
        account_page.wait_load_account()
        account_page.logout()
        with allure.step("Проверяем, что произошел выход из аккаунта"):
            assert login_page.is_displayed(LoginPageLocators.EMAIL_FIELD)
