from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

browser = webdriver.Chrome()

try:
    link = "https://vk.com/"
    browser.get(link)
    
    print(browser.get_cookies())
    print(browser.add_cookie({"id": "1"}))
    print(browser.delete_all_cookies())

finally:
    time.sleep(10)
    browser.quit()