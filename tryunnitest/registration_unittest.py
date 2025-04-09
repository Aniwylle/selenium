from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver import Keys
import time
import unittest


class RegTest(unittest.TestCase):


    def test_open(self):
        browser = webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration1.html")
        time.sleep(2)
        self.assertEqual(browser.find_elements(By.CSS_SELECTOR, "[required]"),"kugkugkug")

    def test_button(self):
        self.assertEqual(browser.find_element(By.CLASS_NAME, value="btn.btn-default").click())
if __name__ == "__main__":
    unittest.main()