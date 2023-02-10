from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
path = Service('D:\Program Files\Python310\Scripts\chromedriver.exe')
driver = Chrome(service=path, options=chrome_options)
driver.get('https://taobao.com')