import time
from pages.form_page import FormPage

def test_login_form(browser):

    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.model_dialog.exist()

    time.sleep(2)
    form_page.first_name.send_keys("John")
    form_page.last_name.send_keys("Doe")
    form_page.user_email.send_keys("<EMAIL>")
    #form_page.gender_radio_1.force_click()#not clickable at all
    form_page.user_number.send_keys("12341234123")
    time.sleep(2)
    #form_page.btn_submit.force_click()
    time.sleep(2)