from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):

    def __init__(self, driver):

        self.base_url = "https://demoqa.com/elements"



        self.label = WebElement(driver, 'div.col-12:nth-child(2)')
        self.icon = WebElement(driver, 'header > a > img')


        self.btn_sidebar_first_textbox = WebElement(driver, '#item-0')
        self.btn_sidebar_first_checkbox = WebElement(driver, '#item-1')
        self.btn_sidebar_first_radiobutton = WebElement(driver, '#item-2')
        self.btn_sidebar_first_webtables = WebElement(driver, '#item-3')
        self.btn_sidebar_first_buttons = WebElement(driver, '#item-4')
        self.btn_sidebar_first_links = WebElement(driver, '#item-5')
        self.btn_sidebar_first_brokenlinks = WebElement(driver, '#item-6')
        self.btn_sidebar_first_uploadanddownload = WebElement(driver, '#item-7')
        self.btn_sidebar_first = WebElement(driver,
                                            'div.element-group:nth-child(1) > span:nth-child(1) > div:nth-child(1)')


        self.btn_sidebar_second_practiceform = WebElement(driver, '.show > ul:nth-child(1) > li:nth-child(1)')
        self.btn_sidebar_second = WebElement(driver,
                                            'div.element-group:nth-child(2) > span:nth-child(1) > div:nth-child(1)')

        super().__init__(driver, self.base_url)