from selenium.webdriver.common.by import By

class BasePageLocators():
    OPEN_ACCOUNT = (By.CLASS_NAME, "wd-tools-icon")
    BUTTON_CREATE_ACCOUNT = (By.CLASS_NAME, "btn.btn-style-link.btn-color-primary.create-account-button")
    SEARCH_BASKET = (By.NAME, "s")
    ARBUZ_F1 = "Арбуз Оранж Кинг F1"
    DELETE_COOKIES = (By.CLASS_NAME, "registration-info")

class MyAccountPageLocators():
    NEWNAME_REG_FORM = (By.ID, "reg_username") 
    # NEWNAME_REG = "DaryaTest6"
    NEWEMAIL_REG_FORM = (By.ID, "reg_email")
    # NEWEMAIL_REG = "DaryaTest6.Ivanova@mail.ru"
    NEWPASSWORD_REG_FORM = (By.ID, "reg_password")
    # NEWPASSWORD_REG = "IvanovaDarya228"
    BUTTON_REG_ACCOUNT = (By.CLASS_NAME, "woocommerce-Button.button.wp-element-button")
    REG_ERROR_TEXT = (By.CLASS_NAME, "woocommerce-notices-wrapper")

    BUTTON_INPUT = (By.CLASS_NAME, "wd-tools-icon")
    NAME_FORM = (By.ID, "username") 
    # INPUT_NAME = "Darya"
    PASSWORD_FORM = (By.ID, "password")
    # INPUT_PASSWORD = "IvanovaDarya228"
    BUTTON_INPUT_ACCOUNT = (By.NAME, "login")
    ACCOUNT_TITTLE = (By.CLASS_NAME,"entry-title.title")

class MainPageLocators():
    pass

class BasketPageLocators():
    SEARCH_SUBMIT = (By.CLASS_NAME, "searchsubmit")
    ADD_BASKET = (By.NAME, "add-to-cart")
    LOOK_BASKET = (By.LINK_TEXT, "ПРОСМОТР КОРЗИНЫ")
    ARBUZ_IN_BASKET = (By.LINK_TEXT,"Арбуз Оранж Кинг F1")
    

