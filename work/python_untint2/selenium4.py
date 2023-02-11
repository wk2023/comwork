from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\data"')
time.sleep(5)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://www.taobao.com')
time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[3]/input').send_keys('坐垫')
time.sleep(5)
browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[1]/button').click()
divlsit = browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div')
print(type(divlsit))
for list_top in divlsit:
    print(list_top.text)