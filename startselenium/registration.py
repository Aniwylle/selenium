from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

try:
    # Запускаем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration1.html")
    time.sleep(2)  # Даём время странице загрузиться

    input_array = browser.find_elements(By.CSS_SELECTOR, "[required]")

    elements = ["Ivan", "Ivanov", "Ivan.Ivanov@mail.ru"]

    for input_element, value in zip(input_array, elements):
        input_element.send_keys(value)

    button_element = browser.find_element(By.CLASS_NAME, value="btn.btn-default")
    button_element.click()

    time.sleep(7)


finally:
    browser.quit()