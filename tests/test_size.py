import time
from pages.swag_labs import SwagLabs

def test_size(browser):
    demoqa_page = SwagLabs(browser)

    demoqa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
