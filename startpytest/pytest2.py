import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By

link = "https://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class")
def browser():
    print("\n start br")
    browser = webdriver.Chrome()
    yield browser
    # код после теста
    print("\n quit br")
    browser.quit()

# @pytest.fixture(autouse=True)
# def prepare_some_data():
#     print("n\ подгатавливает данные")

@pytest.mark.full_class
class TestMainPage():

    @pytest.mark.win10 #чтобы запустить, вписать в cmd: pytest -s -v -m "smoke and win10" pytest2.py 
    @pytest.mark.smoke
    def test_guest(self, browser):
        print("\n start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("\n end test1")

    @pytest.mark.regression
    def test_2(self, browser):
        print("\n start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("\n end test2")