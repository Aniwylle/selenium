from .pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_do_login_page(browser):
    url = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = MainPage(browser, url) #инициализация обьект мейнпейдж, передав в него фикстуру бровсер и сылку юрл
    page.open()
    page.go_to_link_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() 
    # page.should_be_login_link()







# def test_add_to_cart(browser):
#     page = ProductPage(url="", browser) #инициализация PageObject
#     page.open() #открыть страницу
#     page.should_be_add_to_cart_button() #проверить кнопку для добавления
#     page.add_product_to_cart() #жмем кнопку "добавить"
#     page.should_be_succes_message() #проверяем сообщние о добавлении 