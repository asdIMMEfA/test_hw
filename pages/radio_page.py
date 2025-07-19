from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        self.radio_yes = WebElement(driver,
                                    '#yesRadio')
        self.radio_impressive = WebElement(driver,
                                            '#impressiveRadio')
        self.radio_no = WebElement(driver,
                                   '#noRadio')
        self.text_success = WebElement(driver,
                                       '.mt-3')
        super().__init__(driver, self.base_url)