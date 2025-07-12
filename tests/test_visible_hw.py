from pages import elements_page
import time

from pages.elements_page import ElementsPage
from pages.accordion import Accordion


def test_visible_accordion(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()
    assert accordian_page.first_textbox.visible()

    accordian_page.first_textbox_header.click()
    time.sleep(2)
    assert not accordian_page.first_textbox.visible()

def test_visible_accordion_default(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()

    assert not accordian_page.second_textbox_child1.visible()
    assert not accordian_page.second_textbox_child2.visible()
    assert not accordian_page.third_textbox.visible()
