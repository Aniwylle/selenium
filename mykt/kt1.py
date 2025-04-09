from selenium import webdriver
import pytest

class BrowserFixture:
    @pytest.fixture(scope="session")
    def browser(self):
        # Установка браузера по умолчанию
        browser = webdriver.Chrome()
        yield browser
        browser.quit()

    @pytest.fixture(autouse=True)
    def select_browser(self, request):
        if request.config.getoption("--browser") == "firefox":
            browser = webdriver.Firefox()
        else:
            browser = self.browser
        return browser
    
    def test_example(browser):
    # Пример теста, который использует выбранный браузер
        browser.get("http://www.google.com")
        assert "Google" in browser.title