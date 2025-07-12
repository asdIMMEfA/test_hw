from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):

    def __init__(self, driver):

        super().__init__(driver, self.base_url)

        self.base_url = "https://demoqa.com/elements"
        self.label = WebElement(driver, 'div.col-12:nth-child(2)')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.btn_sidebar_first = WebElement(driver, 'div.element-group:nth-child(1) > span:nth-child(1) > div:nth-child(1)')