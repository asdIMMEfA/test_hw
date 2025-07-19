from email.policy import default

from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from components.components import WebElement

class SwagLabs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com'
        super().__init__(driver,self.base_url)
        self.h5 = WebElement(driver, 'html body div#app div.body-height div.home-content div.home-body div.category-cards div.card.mt-4.top-card div div.card-body h5')
        self.btn = WebElement(driver, 'div.card:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer:nth-child(3)')