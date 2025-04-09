from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

try:
    browser.implicitly_wait(5)
    url = "https://workerbntu.github.io/tests/wait2.html"
    browser.get(url)

    # button_element = browser.find_element(By.ID, "verify").click()

    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))).click()

    text = browser.find_element(By.ID, "verify_message").text
    print(text)

finally:
    browser.quit()