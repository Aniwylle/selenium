from .pages.product_page import PageObject
import pytest

@pytest.mark.parametrize("url", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_num1(browser, url):
    page = PageObject(browser, url) 
    page.open()
    page.add_cart()
    page.is_not_element_present()

@pytest.mark.parametrize("url", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_num2(browser, url):
    page = PageObject(browser, url) 
    page.open()
    page.is_not_element_present()

@pytest.mark.parametrize("url", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_num3(browser, url):
    page = PageObject(browser, url) 
    page.open()
    page.add_cart()
    page.is_disappeared()