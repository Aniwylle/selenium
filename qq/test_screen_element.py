from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com")
ul = browser.find_element(By.XPATH, '//*[@id="browse"]/li/ul')
ul.screenshot("ul.png")

browser.quit()