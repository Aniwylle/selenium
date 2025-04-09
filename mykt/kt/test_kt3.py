import pytest
from .pages.main_page import MainPage
from .pages.myaccount_page import MyAccountPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.skip
# тест-кейс на регистрацию нового аккаунта и выход
def test_test1(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.registration_new_account(name="DaryaTest10", email="DaryaTest10.Ivanova@mail.ru", password="IvanovaDarya228")
    page.delete_cookies_and_exit()

@pytest.mark.skip
# тест-кейс на регистрацию существуещего аккаунта
def test_test2(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_be_login_button()
    page.login_button_click()
    page.reg_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.registration_old_account(name="Darya", email="DaryaIvanova@mail.ru", password="IvanovaDarya228")

@pytest.mark.skip
#тест-кейс на вход
def test_test3(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_be_login_button()
    page.login_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.login_in_account(name="Darya", password="IvanovaDarya228")

#тест-кейс на поиск и оформление корзины  
def test_test4(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_search_arbuz_in_catalog()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.look_in_basket()