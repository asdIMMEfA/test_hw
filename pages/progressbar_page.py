from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class ProgressBar(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        self.progressBar = WebElement(driver,
                                          '.progress-bar')
        self.btn = WebElement(driver,
                               '#startStopButton')
        super().__init__(driver, self.base_url)