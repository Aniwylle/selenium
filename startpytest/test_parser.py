from selenium.webdriver.common.by import By
import pytest

link = "https://selenium1py.pythonanywhere.com/"

@pytest.mark.win10
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")