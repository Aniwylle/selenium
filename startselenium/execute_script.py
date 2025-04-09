from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
import math

browser = webdriver.Chrome()

try:
    link = "https://workerbntu.github.io/tests/execute_script.html"
    browser.get(link)

    def func():
        x = (browser.find_element(By.ID, "input_value")).text
        answer = math.log(abs(12 * math.sin(int(x))))
        return answer
    
    boxElement = browser.find_element(By.ID, "answer")
    boxElement.send_keys(func())

    buttonElement = browser.find_element(By.ID, "robotCheckbox")
    buttonElement.click()

    RuleElement = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", RuleElement)
    browser.execute_script("window.scrollBy(0, 100);") 
    RuleElement.click()

    submitElement = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submitElement.click()
  


finally:
    time.sleep(10)
    browser.quit()