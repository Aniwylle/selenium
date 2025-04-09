from .pages.main_page import MainPage
from .pages.myaccount_page import MyAccountPage
import pytest 
from mykt.kt.logger_info import logger

def test_test3_special_fail(browser, jira_client):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_be_login_button()
    page.login_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.login_in_account(name="Darya", password="IvanovaDarya228")
    print(jira_client.projects())
    try:
        assert "буээээ" in page.browser.title, "Тест упал специально"
    except AssertionError as error:
        logger.error(f"{error}")
        raise error


def test_test2(browser, jira_client):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_be_login_button()
    page.login_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.login_in_account(name="Darya", password="IvanovaDarya228")

@pytest.mark.xfail
def test_test3(browser, jira_client):
    url = "https://ogorodnik.by/"
    page = MainPage(browser, url) 
    page.open()   
    page.should_be_login_button()
    page.login_button_click()
    login_page = MyAccountPage(browser, browser.current_url)
    login_page.login_in_account(name="Darya", password="IvanovaDarya228")