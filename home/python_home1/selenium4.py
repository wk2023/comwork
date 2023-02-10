from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
# import os

# os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\data"')
# time.sleep(5)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(options=chrome_options)
# 默认网页已经打开淘宝  否则执行下面语句
# browser.get('http://www.taobao.com')
# time.sleep(3)
# browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[3]/input').send_keys('坐垫')
# time.sleep(5)
# browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]/form/div[1]/button').click()
'''
divlsit = browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div')
print(type(divlsit))
for i in range(0, len(divlsit)):
    print(i)
    # print(divlsit[i].text)
    divshopname = divlsit[i].find_element(By.XPATH, '//a[@class = "J_ClickStat"]')
    print(divshopname.get_attribute('href'))
    '''
for page in range(1,50):
    divtitles = browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/*/*/a')
    divshopname= browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/div[2]/div[3]/div[1]/a')
    divdeal_cnt= browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/div[2]/div[1]/div[2]')
    divpice= browser.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[21]/div/div/div[1]/div/div[2]/div[1]/div[1]/strong')
    for i in range(0, len(divtitles)):
        print(i+1)
        print(divtitles[i].get_attribute('href'))
        print(divtitles[i].text)
        print(divshopname[i].text)
        print(divshopname[i].get_attribute('href'))
        print(divdeal_cnt[i].text)
        print(divpice[i].text)
    next_booten = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[1]/div[26]/div/div/div/ul/li[10]/a')
    next_booten.click()
    time.sleep(5)