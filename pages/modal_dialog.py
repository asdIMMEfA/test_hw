from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.components import WebElement

class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        self.btns_menu = WebElement(driver,
                                          '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver,
                               '#app > header:nth-child(1) > a:nth-child(1)')
        self.small_modalButton = WebElement(driver,
                                            '#showSmallModal')
        self.large_modalButton = WebElement(driver,
                                            '#showLargeModal')
        self.close_small_modalButton = WebElement(driver,
                                                  '#closeSmallModal')
        self.close_large_modalButton = WebElement(driver,
                                                  '#closeLargeModal')
        self.modalDialog = WebElement(driver,
                                      '.modal-dialog')
        super().__init__(driver, self.base_url)