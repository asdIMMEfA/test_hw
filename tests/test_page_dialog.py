import pytest
from selenium.webdriver.common.by import By
from pages.modal_dialog import ModalDialog

def test_modal_elements(browser):

    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()
    assert modal_dialog.btns_menu.check_count_elements(count=5)

def test_navigation_modal(browser):

    modal_dialog = ModalDialog(browser)
    modal_dialog.visit()
    modal_dialog.refresh()
    modal_dialog.icon.click()
    modal_dialog.back()
    browser.set_window_size(900,400)
    modal_dialog.forward()
    assert modal_dialog.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000,1000)
