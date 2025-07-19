from pages.progressbar_page import ProgressBar
import time

def test_progressBar(browser):
    progressBar_page = ProgressBar(browser)

    progressBar_page.visit()
    time.sleep(2)

    assert progressBar_page.progressBar.exist()
    progressBar_page.btn.click()
    while True:
        if progressBar_page.progressBar.get_dom_attribute('aria-valuenow') == '50':
            progressBar_page.btn.click()
            assert True
            break