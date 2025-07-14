from pages.elements_page import ElementsPage
from pages.swag_labs import SwagLabs


def test_navigation(browser):
    demoqa_page = SwagLabs(browser)
    demoqa_page.visit()
    demoqa_page.refresh()
    demoqa_page.back()
    demoqa_page.forward()

    assert demoqa_page.equal_url()
