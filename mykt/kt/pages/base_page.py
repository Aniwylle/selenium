from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from mykt.kt.logger_info import logger

class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.logger = logger

    def open(self):
        self.browser.get(self.url)
        self.logger.info(f"сайт открылся ({self.url})")
        
    def is_element_present(self,how,what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False
        
        return True
    
    def is_not_element_present(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    
    def is_disappeared(self,how,what,timeout=5):
        try:
            WebDriverWait(self.browser,timeout,poll_frequency=TimeoutException).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            return True
        return False
    
    def go_to_link_page(self):
        self.logger.info(f"Перейти на страницу логина ({self.url})")
        login = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login.click()
        # return LoginPage(browser = self.browser,url = self.browser.current_url)

    # def open_basket(self):
    #     login = self.browser.find_element(*BasePageLocators.BUTTON_BASKET)
    #     login.click()

# ниже для ктшки
    def should_be_login_link(self):
        self.logger.info(f"Должна быть ссылка логина ({self.url})")
        try:
            assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Нет ссылки на страницу авторизации"
        except AssertionError as error:
            logger.error(f"{error}")
            raise error
        
    def should_be_login_button(self):
            self.logger.info(f"Должна быть кнопка логина ({self.url})")
            try:
                assert self.is_element_present(*BasePageLocators.OPEN_ACCOUNT), "нет кнопки профиля"
            except AssertionError as error:
                logger.error(f"{error}")
                raise error
        
    
    def login_button_click(self):
        self.logger.info(f"Нажатие кнопки логина ({self.url})")
        self.browser.find_element(*BasePageLocators.OPEN_ACCOUNT).click()

    def should_search_arbuz_in_catalog(self):
        self.logger.info(f"Должен быть поиск арбуза в каталоге ({self.url})")
        self.browser.find_element(*BasePageLocators.SEARCH_BASKET).send_keys(*BasePageLocators.ARBUZ_F1)

    def refresh(self):
        self.browser.refresh()

    def delete_cookies_and_exit(self):
        self.logger.info(f"Удаление печенек, выход с сайта ({self.url})")
        self.browser.delete_all_cookies()
        self.refresh()
        self.browser.find_element(*BasePageLocators.OPEN_ACCOUNT).click()
        try:
            assert self.browser.find_element(*BasePageLocators.DELETE_COOKIES), "не удалось очистить файлы cookie"
        except AssertionError as error:
            logger.error(f"{error}")
            raise error
        

            