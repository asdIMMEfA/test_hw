import pytest

from pages.tables_page import WebTables
import time
def test_webtables(browser):
    webtable_page = WebTables(browser)

    webtable_page.visit()

    webtable_page.table_head_firstname.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_lastname.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_age.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_salary.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_email.click()
    table_list = webtable_page.table_body.find_elements()

    webtable_page.table_head_departament.click()
    table_list = webtable_page.table_body.find_elements()