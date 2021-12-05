from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/verbal-memory')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button').click()


listowords = []

while True:
    word = driver.find_element_by_class_name('word').text
    if word in listowords:
        driver.find_element(By.XPATH, '//button[text()="SEEN"]').click()
    elif word not in listowords:
        driver.find_element(By.XPATH, '//button[text()="NEW"]').click()
        listowords.append(word)
    if int(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]/p/span[2]').text.split()[2]) > 1000000:
        break
while True:
    try:
        driver.find_element(By.XPATH, '//button[text()="Save score"]').click()
        break
    except:useless=1
time.sleep(10)