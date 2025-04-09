from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

options = Options()
options.add_experimental_option("prefs", {"intl.accept_languages": "sv"})

browser = webdriver.Chrome(options=options)
link = "https://google.com"
browser.get(link)

time.sleep(5)