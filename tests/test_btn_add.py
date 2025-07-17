from webdriver_manager.core import driver
from pages.koup_add import KoupAdd
from pages.koup_main import Koup
import time

def test_koup_add(browser):
    koup = Koup(browser)
    koup_add = KoupAdd(browser)
    koup.visit()

    assert koup.add_remove_link.get_text() == 'Add/Remove Elements'
    time.sleep(3)
    koup.add_remove_link.click()
    time.sleep(3)
    assert koup_add.equal_url()


    assert koup_add.btn_add.get_text() == 'Add Element'
    assert koup_add.btn_add.get_dom_attribute('onclick') == "addElement()"

    for i in range(4):
        koup_add.btn_add.click()

    time.sleep(3)
    assert koup_add.btns_delete.check_count_elements(count=4)

    # проверка для всех элементов
    for element in koup_add.btns_delete.find_elements():
        assert element.text == 'Delete'

    # проверка только для первого элемента
    assert koup_add.btns_delete.get_text() == 'Delete'

    while koup_add.btns_delete.exist():
        koup_add.btns_delete.click()

    assert not koup_add.btns_delete.exist()