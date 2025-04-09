from selenium.webdriver.common.by import  By
import time

def test_add_to_cart_button_should_exist(browser):
    url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(url)
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket").is_displayed(), "нет кнопки"
