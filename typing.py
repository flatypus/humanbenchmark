from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/typing')


words = driver.find_elements_by_class_name('incomplete')
textifiedwords = [words[i].text for i in range(len(words))]

word = ''
for _ in textifiedwords:
    if _ == '':
        word+=' '
    else:
        word+=_

typehere = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')
typehere.send_keys(word)
time.sleep(10)
