import allure
import pytest
from selenium import webdriver
from constants.links import Links
from helpers.user import *


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    with allure.step("Создаем экземпляр браузера"):
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
    with allure.step(f"Открываем страницу {Links.MAIN}"):
        driver.get(Links.MAIN)
    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()


@allure.step("Создаём пользователя")
@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = create_user()
    yield user_data
    token = user_login(user_data)
    delete_user(token)


@allure.step("Создаём пользователя и логинимся")
@pytest.fixture(scope="function")
def user_returns_token():
    user_data = create_user()
    token = user_login(user_data)
    yield user_data, token
    delete_user(token)
