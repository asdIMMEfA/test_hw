from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        self.slider = WebElement(driver,
                                          '.range-slider')
        self.imp = WebElement(driver,
                               '#sliderValue')
        super().__init__(driver, self.base_url)