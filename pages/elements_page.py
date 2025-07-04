from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        self.label = WebElement(driver, 'div.col-12:nth-child(2)')
        super().__init__(driver,self.base_url)