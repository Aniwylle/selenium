from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
browser = webdriver.Chrome()

try:
    browser.implicitly_wait(5)
    link = "https://workerbntu.github.io/tests/wait1.html"
    browser.get(link)

    buttonElement = browser.find_element(By.TAG_NAME, "button")
    buttonElement.click()
    assert browser.find_element(By.ID, "verify_message").text == "Verification was successful!" #если все ок assert пропустит, если нет, выдаст ошибку

finally:
    time.sleep(2)
    browser.quit()