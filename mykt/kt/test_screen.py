from .pages.main_page import MainPage
from .pages.myaccount_page import MyAccountPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .utils import screen
from selenium.webdriver.common.by import By
import time

def test_just_screen(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open() 
    time.sleep(2)
    page.browser.save_screenshot("mykt/kt3/screenshots/screen_test.png")
    assert screen.compare_images("mykt/kt3/screenshots/screen_base.png", "mykt/kt3/screenshots/screen_test.png"), "Изображения не совпадают"

def test_element_screen(browser):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()
    time.sleep(2)
    ul = browser.find_element(By.CLASS_NAME, 'vc_column-inner.vc_custom_1651571909539')
    ul.screenshot("mykt/kt3/screenshots/ul_test.png")
    assert screen.compare_images("mykt/kt3/screenshots/ul_base.png", "mykt/kt3/screenshots/ul_test.png"), "Изображения элементов не совпадают"