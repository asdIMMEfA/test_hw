from pages.slider_page import Slider
from selenium.webdriver.common.keys import Keys

def test_slider(browser):
    slider = Slider(browser)

    slider.visit()

    assert slider.slider.exist()

    while slider.imp.get_dom_attribute('value') != '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.imp.get_dom_attribute('value') == '50'