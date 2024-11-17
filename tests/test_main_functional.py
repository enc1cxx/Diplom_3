import time
import allure
from locators.main_page_locators import MainPageLocators
from locators.constructor_page_locators import ConstructorPageLocators
from locators.orders_page_locators import OrderPageLocators
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic("Stellar Burger")
@allure.feature("Проверки основного функционала")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Алексей Александров")
class TestMainFunctional:

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Проверяем, что произошел переход в конструктор")
    def test_follow_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_constructor()
        with allure.step("Проверяем, что произошел переход в конструктор"):
            assert main_page.is_displayed(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.title("Переход по клику на «Лента заказов»")
    @allure.description("Проверяем, что произошел переход в ленту заказов")
    def test_follow_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_page = OrderFeedPage(driver)
        order_page.wait_load_order_page()
        with allure.step("Проверяем, что произошел переход в ленту заказов"):
            assert main_page.is_displayed(OrderPageLocators.ORDER_FEED_HEADER)

    @allure.title("Отображение модалки с информацией об ингредиенте")
    @allure.description(
        "Проверяем, что отображается табличка с информацией об ингредиенте"
    )
    def test_info_about_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.push_to_ingredient()
        with allure.step(
            "Проверяем, что отображается табличка с информацией об ингредиенте"
        ):
            assert constructor_page.is_displayed(
                ConstructorPageLocators.INFO_ABOUT_INGREDIENT
            )

    @allure.title("Закрытие модалки с информацией об ингредиенте")
    @allure.description(
        "Проверяем, что табличка с информацией об ингредиенте закрылась и не отображается"
    )
    def test_close_info_about_ingredient(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.push_to_ingredient()
        constructor_page.close_ingredient_info()
        with allure.step(
            "Проверяем, что табличка с информацией об ингредиенте закрылась и не отображается"
        ):
            assert not constructor_page.is_displayed(
                ConstructorPageLocators.INFO_ABOUT_INGREDIENT
            )

    # Пробовал разное, но на Firefox drag_and_drop работать не захотел ни через js, ни через ActionChains
    @allure.title("Счетчик ингредиентов")
    @allure.description(
        "Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается"
    )
    def test_ingredient_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_visibility(ConstructorPageLocators.FLUO_BUN_COUNTER)
        with allure.step("Проверяем, что счетчик Флюоресцентных булок == 0"):
            assert (
                constructor_page.text_in_element(
                    ConstructorPageLocators.FLUO_BUN_COUNTER
                )
                == "0"
            )
        constructor_page.add_fluo_bun()
        with allure.step("Проверяем, что счетчик Флюоресцентных булок == 2"):
            assert (
                constructor_page.text_in_element(
                    ConstructorPageLocators.FLUO_BUN_COUNTER
                )
                == "2"
            )

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description(
        "Проверяем, что табличка с заголовком 'Идентификатор заказа' отображается после оформления "
        "заказа"
    )
    def test_create_order(self, driver, create_and_delete_user):
        main_page = MainPage(driver)
        main_page.go_to_login_form()
        login_page = LoginPage(driver)
        login_page.login(
            create_and_delete_user["email"], create_and_delete_user["password"]
        )
        constructor_page = ConstructorPage(driver)
        constructor_page.add_fluo_bun()
        constructor_page.place_an_order()
        with allure.step(
            "Проверяем, что табличка с заголовком Идентификатор заказа отображается"
        ):
            assert constructor_page.is_displayed(
                ConstructorPageLocators.CREATE_ID_HEADER
            )
