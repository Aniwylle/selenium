from selenium import webdriver
from selenium.webdriver.common.by import  By
import pytest

link = "https://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class") #Можно задать область видимости
def browser():
    print("Запуск браузера")
    browser = webdriver.Chrome()
    yield browser
    #код после теста
    print("Закрытие браузера")
    browser.quit

@pytest.fixture(autouse=True)
def prepairData():
    print("\n Подготовка данных")

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\n start browser")
        self.browser = webdriver.Chrome()

    @classmethod
    def setup_class(self):
        print("\n quit browser")
        self.browser.quit()

    def test_guest(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest2(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

class TestMainPage2():

    def setup_method(self):
        print("\n start browser")
        self.browser = webdriver.Chrome()

    def setup_method(self):
        print("\n quit browser")
        self.browser.quit()

    def test_guest(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest2(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini.btn-group > a")