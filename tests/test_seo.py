from pages.elements_page import ElementsPage
from pages.swag_labs import SwagLabs


def test_check_title_demo(browser):
    demoqa_page = SwagLabs(browser)
    demoqa_page.visit()
    assert browser.title == 'DEMOQA'