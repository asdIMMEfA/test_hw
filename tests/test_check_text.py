from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


from conftest import browser
from pages.elements_page import ElementsPage
from pages.swag_labs import SwagLabs

def test_check_footer_text(browser):
    page = SwagLabs(browser)
    page.visit()
    assert page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_elements_text(browser):
    demo_qa_page = SwagLabs(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()

    time.sleep(3)
    assert demo_qa_page.equal_url()
    demo_qa_page.click_on_the_btn()
    assert elements_page.equal_url()

    assert elements_page.label.get_text() == 'Please select an item from left to start practice.'