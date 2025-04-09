from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    browser.implicitly_wait(5)
    url = "https://ogorodnik.by/"
    browser.get(url)

    # тест-кейс на регистрацию нового аккаунта и выход
    browser.find_element(By.CLASS_NAME, "wd-tools-icon").click()
    browser.find_element(By.CLASS_NAME, "btn.btn-style-link.btn-color-primary.create-account-button").click()
    browser.find_element(By.ID, "reg_username").send_keys("Darya")
    browser.find_element(By.ID, "reg_email").send_keys("Darya.Ivanova@mail.ru")
    browser.find_element(By.ID, "reg_password").send_keys("IvanovaDarya228") 
    browser.find_element(By.CLASS_NAME, "woocommerce-Button.button.wp-element-button").click()
    assert browser.find_element(By.CLASS_NAME,"entry-title.title").text == "Личный кабинет"
    browser.delete_all_cookies()
    browser.get(url)
    browser.find_element(By.CLASS_NAME, "wd-tools-icon").click()
    assert browser.find_element(By.LINK_TEXT, "СОЗДАТЬ АККАУНТ").text == "СОЗДАТЬ АККАУНТ"

    # тест-кейс на регистрацию существуещего аккаунта
    browser.find_element(By.CLASS_NAME, "btn.btn-style-link.btn-color-primary.create-account-button").click()
    browser.find_element(By.ID, "reg_username").send_keys("Ivan") 
    browser.find_element(By.ID, "reg_email").send_keys("Ivan.Ivanov@mail.ru") 
    browser.find_element(By.ID, "reg_password").send_keys("Ivanov228") 
    browser.find_element(By.CLASS_NAME, "woocommerce-Button.button.wp-element-button").click()
    assert browser.find_element(By.CLASS_NAME, "showlogin").text == "Войти."

    #тест-кейс на вход
    browser.find_element(By.CLASS_NAME, "wd-tools-icon").click()
    browser.find_element(By.ID, "username").send_keys("Ivan")   
    browser.find_element(By.ID, "password").send_keys("Ivanov228") 
    browser.find_element(By.NAME, "login").click()
    assert browser.find_element(By.CLASS_NAME,"entry-title.title").text == "Личный кабинет" 


    #тест-кейс на поиск и оформление корзины    
    browser.find_element(By.NAME, "s").send_keys("арбуз")
    browser.find_element(By.CLASS_NAME, "searchsubmit").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[4]/div[2]/div/div[2]/div/a").click()
    browser.find_element(By.LINK_TEXT, "ПРОСМОТР КОРЗИНЫ").click()
    browser.execute_script("window.scrollBy(0, 100);") 
    assert browser.find_element(By.LINK_TEXT, "Арбуз Оранж Кинг F1").text == "Арбуз Оранж Кинг F1" #здесь поменяла как вы попросили

finally:
    time.sleep(5)
    browser.quit()