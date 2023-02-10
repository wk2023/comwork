from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
# print(browser.page_source)
time.sleep(10)
booutl = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[3]/input')
booutl.send_keys('坐垫')
time.sleep(5)
boout2 = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[1]/button')
boout2.click()
time.sleep(5)
browser.quit()