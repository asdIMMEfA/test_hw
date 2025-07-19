import pytest



@pytest.mark.smoke
def test_decor1(browser):
    assert True

@pytest.mark.regress
def test_decor2(browser):
    assert True

@pytest.mark.regress
def test_decor3(browser):
    assert True

@pytest.mark.regress
def test_decor4(browser):
    assert True