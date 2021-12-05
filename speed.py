from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/reactiontime')
time.sleep(20)
def runagain():
    screen = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]')
    screen.click()
    while True:
        try:
            if driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/h1/div').text == 'Click!':
                screen.click()
                screen.click()
        except:
            try:
                score = int(driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div[2]/h1').text[:-2])
                print(score)
                if score > 20:
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[2]').click()
                    runagain()
                elif score < 21:
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]').click()
                    time.sleep(5)
                    driver.get('https://humanbenchmark.com/tests/reactiontime')
                    runagain()
            except:useless=1
runagain()
time.sleep(100)
driver.quit()