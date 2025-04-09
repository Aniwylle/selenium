import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action="store", default="chrome", help="Выберите браузер: chrome или firefox")

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="sv", help="Выберите язык: en или ru")

    
@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=Options)
    yield browser
    browser.quit


# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "firefox":
#         print("\n Запуск браузера Firefox")
#         browser = webdriver.Firefox()
#     elif browser_name == "chrome":
#         print("\n Запуск браузера Chrome")
#         browser = webdriver.Chrome()  
#     else: 
#         raise pytest.UsageError("--browser_name должен быть Firefox или Chrome")      
#     yield browser
#     #код после теста
#     print("\n Закрытие браузера")
#     browser.quit


