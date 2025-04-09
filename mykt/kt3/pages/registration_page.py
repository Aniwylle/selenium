from .locators import RegistratePageLocators
from .locators import BasePageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    def registration_new_account(self):
        self.browser.find_element(*BasePageLocators.OPEN_ACCOUNT).click()
        self.browser.find_element(*BasePageLocators.BUTTON_CREATE_ACCOUNT).click()
        self.browser.find_element(*RegistratePageLocators.NAME_REG_FORM).send_keys("Darya1")
        self.browser.find_element(*RegistratePageLocators.EMAIL_REG_FORM).send_keys("Darya1.Ivanova@mail.ru")
        self.browser.find_element(*RegistratePageLocators.PASSWORD_REG_FORM).send_keys("IvanovaDarya228") 
        self.browser.find_element(*RegistratePageLocators.BUTTON_REG_ACCOUNT).click()
        assert self.browser.find_element(By.CLASS_NAME,"entry-title.title").text == "Личный кабинет"

    # def shoud_product_add_to_cart(self):
    #     add_to_cart = self.browser.find_element(*PageObjectLocators.ADD_TO_CART_TEXT)
    #     name_book = self.browser.find_element(*PageObjectLocators.NAME_BOOK)
    #     assert name_book.text == add_to_cart.text, "Товар не был добавлен в корзину"

    # def shoud_product_price_and_cart(self):
    #     price_cart = self.browser.find_element(*PageObjectLocators.PRICE_CART)
    #     price_book = self.browser.find_element(*PageObjectLocators.PRICE_BOOK)
    #     assert price_book.text in price_cart.text, "Цена товара и сумма корзины не совпали"
    
    # def shoud_is_not_result_message(self):
    #     result = self.is_not_element_present(*PageObjectLocators.ADD_TO_CART_TEXT_FULL)
    #     assert result, "Есть успех, хотя его быть не должно"

    # def shoud_is_desapperared(self):
    #     result = self.is_disappeared(*PageObjectLocators.ADD_TO_CART_TEXT_FULL)
    #     assert result, "Успех не исчез"