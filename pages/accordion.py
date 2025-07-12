from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):

        self.base_url = "https://demoqa.com/accordian"

        self.first_textbox = WebElement(driver, '#section1Content > p')
        self.first_textbox_header = WebElement(driver, '#section1Heading')

        self.second_textbox = WebElement(driver, '#section2Content > p')
        self.second_textbox_child1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.second_textbox_child2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.second_textbox_header = WebElement(driver, '#section2Heading')

        self.third_textbox = WebElement(driver, '#section3Content > p')
        self.third_textbox_header = WebElement(driver, '#section3Heading')
        super().__init__(driver, self.base_url)