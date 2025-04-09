from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import math

browser = webdriver.Chrome()

try:
    link = "https://workerbntu.github.io/tests/redirect_accept.html"
    browser.get(link)

    buttonElement = browser.find_element(By.TAG_NAME, "button")
    buttonElement.click()
    
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    x = (browser.find_element(By.ID, "input_value")).text
    browser.find_element(By.ID, "answer").send_keys(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()


finally:
    time.sleep(10)
    browser.quit()