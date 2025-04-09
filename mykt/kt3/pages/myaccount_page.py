from .locators import MyAccountPageLocators
from .locators import BasePageLocators
from .base_page import BasePage
# ввести данные отдельно под name email password чтобы было на тесте
class MyAccountPage(BasePage):
    def registration_new_account(self, name, email, password):
        self.browser.find_element(*MyAccountPageLocators.NEWNAME_REG_FORM).send_keys(name)
        self.browser.find_element(*MyAccountPageLocators.NEWEMAIL_REG_FORM).send_keys(email)
        self.browser.find_element(*MyAccountPageLocators.NEWPASSWORD_REG_FORM).send_keys(password)
        self.browser.find_element(*MyAccountPageLocators.BUTTON_REG_ACCOUNT).click()
        assert self.browser.find_element(*MyAccountPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет", "при регистрации нового аккаунта произошла ошибка"

    def login_in_account(self, name, password):
        self.browser.find_element(*MyAccountPageLocators.NAME_FORM).send_keys(name)
        self.browser.find_element(*MyAccountPageLocators.PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*MyAccountPageLocators.BUTTON_INPUT_ACCOUNT).click()
        self.browser.find_element(*BasePageLocators.OPEN_ACCOUNT).click()
        assert self.browser.find_element(*MyAccountPageLocators.ACCOUNT_TITTLE).text == "Личный кабинет", "при в входе в акаунт что-то пошло не так"

    def registration_old_account(self, name, email, password):
        self.browser.find_element(*MyAccountPageLocators.NEWNAME_REG_FORM).send_keys(name)
        self.browser.find_element(*MyAccountPageLocators.NEWEMAIL_REG_FORM).send_keys(email)
        self.browser.find_element(*MyAccountPageLocators.NEWPASSWORD_REG_FORM).send_keys(password)
        self.browser.find_element(*MyAccountPageLocators.BUTTON_REG_ACCOUNT).click()
        print(self.browser.find_element(*MyAccountPageLocators.REG_ERROR_TEXT).text)
        assert self.browser.find_element(*MyAccountPageLocators.REG_ERROR_TEXT).text == "Ошибка: Аккаунт с таким именем пользователя уже зарегистрирован. Пожалуйста, выберите другое имя." or self.browser.find_element(*MyAccountPageLocators.REG_ERROR_TEXT).text == "Ошибка: Учётная запись под таким адресом электронной почты уже зарегистрирована. Войти.", "при создании существуещего аккаунта произошла ошибка"
