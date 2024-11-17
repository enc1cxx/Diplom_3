import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(locator)
        )

    def push_element(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def get_element_attribute(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    def get_current_url(self):
        return self.driver.current_url

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def get(self, link):
        with allure.step(f"Переходим по ссылке {link}"):
            self.driver.get(link)

    def text_in_element(self, locator):
        return self.driver.find_element(*locator).text
