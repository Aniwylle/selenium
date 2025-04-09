from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"https://selenium1py.pythonanywhere.com/{language}"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_navbar(self, browser, language):
        link = f"https://selenium1py.pythonanywhere.com/{language}"
        browser.get(link)

(["305763", "643051", "003388", "756480", "704777", "376026", "641158", "362417", "641158", "968992", "210864", "586451", "224592", "385461", "809857", "132869", "190051", "986293", "623566", "356349", "385461", "441456"])

def test_guest_should_see_login_link(browser, link_text):
    link = f"https://suninjuly.github.io/find_link_text"
    browser.get(link)
    browser.find_element(By.LINK_TEXT, link_text).click()

