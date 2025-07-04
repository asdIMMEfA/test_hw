from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class WebElement():
    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator

    # переопределение функции find_element
    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.driver.find_element().click()

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)