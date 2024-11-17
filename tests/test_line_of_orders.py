import allure
from constants.links import Links
from helpers.order import create_order
from locators.orders_page_locators import OrderPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic("Stellar Burger")
@allure.feature("Проверки раздела «Лента заказов»")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Алексей Александров")
class TestRestorePassword:

    @allure.title("Детали о заказе")
    @allure.description(
        "Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями"
    )
    def test_info_about_order(self, driver):
        main_page = MainPage(driver)
        main_page.get(Links.MAIN)
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_load_order_page()
        order_feed_page.click_to_newer_order()
        with allure.step("Проверяем, что открылось всплывающее окно с деталями заказа"):
            assert order_feed_page.is_displayed(OrderPageLocators.STRUCTURE_HEADER)

    @allure.title("Отображение заказов пользователя")
    @allure.description(
        "Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице "
        "«Лента заказов»"
    )
    def test_follow_to_restore_password(self, driver, user_returns_token):
        main_page = MainPage(driver)
        main_page.get(Links.MAIN)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            user_returns_token[0]["email"], user_returns_token[0]["password"]
        )
        number = create_order(user_returns_token[1])
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_load_order_page()
        with allure.step(
            "Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице "
            "«Лента заказов»"
        ):
            assert number in order_feed_page.text_in_element(
                OrderPageLocators.NUMBER_OF_ORDER
            )

    @allure.title("Счетчик за все время")
    @allure.description(
        "Проверяем, что при создании нового заказа счётчик 'Выполнено за всё время увеличивается'"
    )
    def test_all_time_order_counter(self, driver, user_returns_token):
        main_page = MainPage(driver)
        main_page.get(Links.MAIN)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            user_returns_token[0]["email"], user_returns_token[0]["password"]
        )
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_load_order_page()
        current_count = order_feed_page.get_all_time_count()
        create_order(user_returns_token[1])
        with allure.step(
            "Проверяем, что при создании нового заказа счётчик 'Выполнено за всё время увеличивается'"
        ):
            assert int(current_count) + 1 == int(
                order_feed_page.get_all_time_count()
            )

    @allure.title("Счетчик за сегодня")
    @allure.description(
        "Проверяем, что при создании нового заказа счётчик 'Выполнено за сегодня увеличивается'"
    )
    def test_today_order_counter(self, driver, user_returns_token):
        main_page = MainPage(driver)
        main_page.get(Links.MAIN)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            user_returns_token[0]["email"], user_returns_token[0]["password"]
        )
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_load_order_page()
        current_count = order_feed_page.get_today_count()
        create_order(user_returns_token[1])
        with allure.step(
            "Проверяем, что при создании нового заказа счётчик 'Выполнено за сегодня увеличивается'"
        ):
            assert int(current_count) + 1 == int(
                order_feed_page.get_today_count()
            )

    @allure.title("Счетчик за сегодня")
    @allure.description(
        "Проверяем, что при создании нового заказа счётчик 'Выполнено за сегодня увеличивается'"
    )
    def test_today_order_counter__(self, driver, user_returns_token):
        main_page = MainPage(driver)
        main_page.get(Links.MAIN)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            user_returns_token[0]["email"], user_returns_token[0]["password"]
        )
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_load_order_page()
        number_of_order = create_order(user_returns_token[1])
        order_feed_page.wait_not_all_orders_done()

        with allure.step(
            "Проверяем, что после оформления заказа его номер появляется в разделе 'В работе'"
        ):
            text = order_feed_page.get_order_in_progress()
            assert number_of_order in text
