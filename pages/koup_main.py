from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from components.components import WebElement

class Koup(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com'
        super().__init__(driver,self.base_url)
        self.add_remove_link = WebElement(driver,
                                          '#content > ul:nth-child(4) > li:nth-child(2) > a:nth-child(1)')