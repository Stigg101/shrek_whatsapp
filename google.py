from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(r"C:/Webdrivers/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

fecker_name = 'Emeul Botha'
loaded = 0

def pageload():
    getUser = driver.find_elements_by_xpath("//*[contains(text(), '" + fecker_name + "')]")
    if len(getUser)>0:
        time.sleep(4)
        getUser[0].click()
        global loaded
        loaded = 1

while loaded == 0:
    pageload()
    print('Please scan QR code')
    time.sleep(2)

shrek =[]
with open('shrek.txt', 'r') as f:
    for line in f.readlines():
        for word in line.split():
            actions = ActionChains(driver)
            actions.send_keys(word, Keys.ENTER)
            actions.perform()
            time.sleep(1)
