from pages.elements_page import ElementsPage
from pages.swag_labs import SwagLabs
from pages.accordion import Accordion
from pages.alert_page import AlertPage
from pages.swag_labs import SwagLabs
from pages.browser_tab import BrowserTab
import pytest
import time

@pytest.mark.parametrize("pages", [Accordion, AlertPage, SwagLabs, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'