from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators
from mykt.kt.logger_info import logger

class BasketPage(BasePage): 
    def look_in_basket(self):
        self.logger = logger
        self.logger.info(f"Просмотр корзины ({self.url})")
        try:
            assert self.browser.find_element(*BasketPageLocators.ARBUZ_IN_BASKET).text == BasePageLocators.ARBUZ_F1
        except AssertionError as error:
            logger.error(f"{error}")
            raise error
        
        