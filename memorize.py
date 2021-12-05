from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/number-memory')
time.sleep(1)

driver.find_element(By.XPATH, '//button[text()="Start"]').click()

while True:
    number = driver.find_element_by_class_name('big-number').text
    if len(number) > 200:
        break
    while True:
        try:
            it = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')
            break
        except:useless = 1
    it.click()
    it.send_keys(number)
    it.send_keys(Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button').click()
            break
        except:useless = 1
    
while True:
    time.sleep(20)
