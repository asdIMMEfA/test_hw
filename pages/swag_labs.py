from email.policy import default

from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from components.components import WebElement

class SwagLabs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com'
        super().__init__(driver,self.base_url)
        #demoqa website elements here
        self.btn = WebElement(driver, 'div.card:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer:nth-child(3)')

    # def exist_icon(self):
    #     try:
    #         self.icon.exist()
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def exist_name_field(self):
    #     try:
    #         self.name_field.exist()
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def exist_login_field(self):
    #     try:
    #         self.login_field.exist()
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    def click_on_the_btn(self):
        self.btn.find_element().click()

    # def exist_footer(self):
    #     try:
    #         self.footer.exist()
    #     except NoSuchElementException:
    #         return False
    #     return True