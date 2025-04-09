from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators

class BasketPage(BasePage): 
    def look_in_basket(self):
        assert self.browser.find_element(*BasketPageLocators.ARBUZ_IN_BASKET).text == BasePageLocators.ARBUZ_F1