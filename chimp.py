from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/chimp')
time.sleep(1)
driver.find_element(By.XPATH, '//button[text()="Start Test"]').click()
while True:
    try:
        buttons = driver.find_elements_by_class_name('css-19b5rdt')
        order = [buttons[_].text for _ in range(len(buttons))]
        for _ in range(1,(len(buttons)+1)):
            buttons[order.index(str(_))].click()
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button').click()
    except:
        break
time.sleep(20)