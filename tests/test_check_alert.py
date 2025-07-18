from pages import alert_page
from pages.alert_page import AlertPage
import time
from selenium.common import NoSuchElementException
from components.components import WebElement
from pages.base_page import BasePage


def test_check_alert(browser):
    alertPage = AlertPage(browser)
    alertPage.visit()
    alertPage.alertButton .click()
    time.sleep(5)
    assert alertPage.alert()
