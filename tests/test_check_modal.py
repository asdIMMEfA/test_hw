from pages.elements_page import ElementsPage
from pages.modal_dialog import ModalDialog
from selenium.common import NoSuchElementException
from components.components import WebElement
from pages.base_page import BasePage
import pytest
import time

def test_check_title_all_pages(browser):
    modal_page = ModalDialog(browser)

    modal_page.visit()
    if not modal_page.equal_url():
        pytest.skip("404 code error.")

    assert modal_page.small_modalButton.exist()
    assert modal_page.large_modalButton.exist()

    modal_page.small_modalButton.click()
    time.sleep(2)
    assert modal_page.close_small_modalButton.exist()
    modal_page.close_small_modalButton.click()
    time.sleep(2)
    assert not modal_page.close_small_modalButton.exist()

    modal_page.large_modalButton.click()
    time.sleep(2)
    assert modal_page.close_large_modalButton.exist()
    modal_page.close_large_modalButton.click()
    time.sleep(2)
    assert not modal_page.close_large_modalButton.exist()


