import time

from selenium.webdriver.common.by import By

from pages.form_page import FormPage

def test_login_form(browser):

    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.model_dialog.exist()

    time.sleep(2)
    form_page.first_name.send_keys("John")
    form_page.last_name.send_keys("Doe")
    form_page.user_email.send_keys("<EMAIL>")
    form_page.hobbies.send_keys("Hobby")
    form_page.current_address.send_keys("123456")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("12341234123")
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.model_dialog.exist()
    form_page.btn_close_model.click_force()

def test_login_form2(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.model_dialog.exist()

    time.sleep(2)
    form_page.state_dropdown_btn.click()
    if form_page.state_first_item.visible():
        form_page.state_first_item.click()

    form_page.city_dropdown_btn.click()
    if form_page.city_first_item.visible():
        form_page.city_first_item.click()
    time.sleep(2)

    assert not form_page.model_dialog.exist()