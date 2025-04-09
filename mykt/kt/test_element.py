from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://ogorodnik.by/")
ul = browser.find_element(By.CLASS_NAME, 'vc_column-inner.vc_custom_1651571909539')
ul.screenshot("selenium/kt3/ul.png")

browser.quit()