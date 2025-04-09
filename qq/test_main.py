import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

@pytest.mark.skip
def test_guest_go_to_login_page(browser):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page = BasePage(browser, url)
    page.open()
    page.should_be_login_link()
    page.go_to_link_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    url = ("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    page = MainPage(browser, url)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.is_basket_empty_message()
    




