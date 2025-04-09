from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    link = "https://workerbntu.github.io/tests/alert_accept.html"
    browser.get(link)
    time.sleep(2)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    browser.switch_to.alert.accept()

    x = (browser.find_element(By.ID, "input_value")).text
    browser.find_element(By.ID, "answer").send_keys(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()


finally:
    time.sleep(10)
    browser.quit()