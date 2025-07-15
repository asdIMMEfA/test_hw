import time

import pytest

from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.name.send_keys('tester')
    text_box.address.send_keys('asdasdasd')
    time.sleep(2)
    text_box.btn_submit.click()
    time.sleep(2)
    # name
    assert text_box.displayed_info.visible()

    info_list = text_box.displayed_info.get_text()

    string1 = info_list[info_list.find(':',1)+1 : info_list.find("\n",1)]
    string2 = info_list[info_list.find(':', info_list.find(':',1) + 1)+1 : len(info_list)]

    assert string1 == ('tester')
    assert string2 == ('asdasdasd')
