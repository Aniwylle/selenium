from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def reg_button_click(self):
        self.logger.info(f"Кнопка регистрации ({self.url})")
        self.browser.find_element(*BasePageLocators.BUTTON_CREATE_ACCOUNT).click()

