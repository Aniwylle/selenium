from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver import Keys
import time

try:
    # Запускаем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_link_text")
    time.sleep(2)  # Даём время странице загрузиться

    input_class = browser.find_element(By.LINK_TEXT, value='224592')
    input_class.click()

    input_FirstName = browser.find_element(By.NAME, value='first_name')
    input_FirstName.send_keys("Ivan")

    input_LastName = browser.find_element(By.NAME, value='last_name')
    input_LastName.send_keys("Petrov")

    input_City = browser.find_element(By.NAME, value='firstname')
    input_City.send_keys("Smolensk")

    input_Country = browser.find_element(By.ID, value='country')
    input_Country.send_keys("Russia")

    button_element = browser.find_element(By.CLASS_NAME, value="btn.btn-default")
    button_element.click()

    time.sleep(7)


finally:
    browser.quit()