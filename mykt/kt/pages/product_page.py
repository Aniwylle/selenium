from .base_page import BasePage
from .locators import BasketPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self):
        self.browser.find_element(*BasketPageLocators.ADD_BASKET).click()
        self.browser.find_element(*BasketPageLocators.LOOK_BASKET).click()