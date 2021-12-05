from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/reactiontime')
#time.sleep(20)
def runagain():
    screen = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]')
    screen.click()
    while True:
        if len(driver.find_elements_by_class_name('view-go e18o0sx0 css-saet2v e19owgy77'))>0:
            screen.click()
            screen.click()

runagain()
time.sleep(100)
driver.quit()