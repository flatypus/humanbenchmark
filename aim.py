from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/aim')
#time.sleep(20)
while True:
    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/div/div/div[6]').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div/div/div[6]').click()
        except:
            break
time.sleep(10)