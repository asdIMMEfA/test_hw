from pages import elements_page
import time

from pages.elements_page import ElementsPage


def test_visible_btn_sidebar(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    time.sleep(2)
    assert el_page.btn_sidebar_first_textbox.visible()

def test_not_visible_btn_sidebar(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    assert el_page.btn_sidebar_first_checkbox.visible()
    if el_page.btn_sidebar_first.exist():
        el_page.btn_sidebar_first.click()
    time.sleep(2)
    assert el_page.btn_sidebar_first_checkbox.not_visible()
