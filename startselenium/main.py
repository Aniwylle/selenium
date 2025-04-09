from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver import Keys
import time

import time

try:
    # Запускаем браузер
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/simple_form_find_task.html")
    # time.sleep(3)  # Даём время странице загрузиться

    input_FirstName = browser.find_element(By.NAME, value='first_name')
    input_FirstName.send_keys("Ivan")

    input_LastName = browser.find_element(By.NAME, value='last_name')
    input_LastName.send_keys("Petrov")

    input_City = browser.find_element(By.NAME, value='firstname')
    input_City.send_keys("Smolensk")

    input_Country = browser.find_element(By.ID, value='country')
    input_Country.send_keys("Russia")

    button_element = browser.find_element(By.ID, value="submit_button")
    button_element.click()

    time.sleep(7)
    # input_element.send_keys(Keys.RETURN)
    # button_element.click()
    # time.sleep(5)
    # result_list = browser.find_elements(By.CSS_SELECTOR, value="#search-result li")
    # for li in result_list:
    #     print(li.text)

finally:
    browser.quit()


# print(browser.find_element(By.ID, value="text"))
# print(browser.find_element(By.CSS_SELECTOR, value='#text'))
# print(browser.find_element(By.XPATH, value='//input'))
# print(browser.find_element(By.NAME, value='text'))
# print(browser.find_element(By.TAG_NAME, value='input'))
# print(browser.find_element(By.CLASS_NAME, value='search3__input'))
# print(browser.find_element(By.LINK_TEXT, value='Войти'))
# print(browser.find_element(By.PARTIAL_LINK_TEXT, value='Во'))

# button_element = browser.find_element(By.CSS_SELECTOR, value="[type='submit']")