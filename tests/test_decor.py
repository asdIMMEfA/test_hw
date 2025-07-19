import time
import pytest
from pages.swag_labs import SwagLabs
from pages.radio_page import Radio
from selenium.webdriver.common.keys import Keys

@pytest.mark.skip(reason='')
def test_decor(browser):
    demoqa_page = SwagLabs(browser)

    demoqa_page.visit()

    assert demoqa_page.h5.check_count_elements(count=6)

    for element in demoqa_page.h5.find_elements():
        assert element.text != ''

@pytest.mark.skipif(True, reason='')
def test_decor_1(browser):
    radio_page = Radio(browser)

    radio_page.visit()

    radio_page.radio_yes.send_keys(Keys.ENTER)
    radio_page.radio_yes.send_keys(Keys.ENTER)
    time.sleep(2)
    assert radio_page.text_success.get_text() == 'You have selected Yes'

    radio_page.radio_impressive.send_keys(Keys.ENTER)
    assert radio_page.text_success.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio_page.radio_no.get_dom_attribute('class')