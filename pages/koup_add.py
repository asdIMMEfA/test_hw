from pages.base_page import BasePage
from selenium.common import NoSuchElementException
from components.components import WebElement

class KoupAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements'
        self.btn_add = WebElement(driver,'.example > button:nth-child(1)')

        self.btns_delete = WebElement(driver,'button.added-manually')
        self.btn_delete1 = WebElement(driver,
                                          'button.added-manually:nth-child(1)')
        self.btn_delete2 = WebElement(driver,
                                      'button.added-manually:nth-child(2)')
        self.btn_delete3 = WebElement(driver,
                                      'button.added-manually:nth-child(3)')
        self.btn_delete4 = WebElement(driver,
                                      'button.added-manually:nth-child(4)')
        super().__init__(driver, self.base_url)