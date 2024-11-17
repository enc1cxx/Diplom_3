import allure
from selenium.webdriver import ActionChains
from locators.constructor_page_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_fluo_bun(self):
        with allure.step("Добавляем флюоресцентную булку в конструктор бургера"):
            bun = self.driver.find_element(*ConstructorPageLocators.FLUO_BUN)
            burger_constructor = self.driver.find_element(
                *ConstructorPageLocators.BURGER_CONSTRUCTOR
            )
            ActionChains(self.driver).drag_and_drop(bun, burger_constructor).perform()

    def push_to_ingredient(self):
        with allure.step("Нажимаем на карточку ингредиента"):
            self.push_element(ConstructorPageLocators.FLUO_BUN)
            self.wait_visibility(ConstructorPageLocators.INFO_ABOUT_INGREDIENT)

    def close_ingredient_info(self):
        with allure.step("Закрываем карточку с информацией об ингредиенте"):
            self.push_element(ConstructorPageLocators.CLOSE_INFO)
            self.wait_invisibility(ConstructorPageLocators.INFO_ABOUT_INGREDIENT)

    def place_an_order(self):
        with allure.step("Нажимаем на кнопку Оформить заказ"):
            self.push_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)
            self.wait_visibility(ConstructorPageLocators.CREATE_ID_HEADER)
