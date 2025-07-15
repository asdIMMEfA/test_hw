from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(self.driver, '#userName')
        self.email = WebElement(self.driver, '#userEmail')
        self.address = WebElement(self.driver, '#currentAddress')
        self.permanent_address = WebElement(self.driver, '#permanentAddress')
        self.btn_submit = WebElement(self.driver, '#submit')

        self.displayed_info = WebElement(self.driver, '.border')
