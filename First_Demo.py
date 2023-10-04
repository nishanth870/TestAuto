import time

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


oj = webdriver.ChromeOptions()
oj.add_argument("--start-maximized")
oj.add_argument('--headless')                          # ---headless browser
#oj.add_argument("--windoe-size=375,667")

obj = Service()
driver = webdriver.Chrome(service=obj, options=oj)
driver.set_window_size(375,667)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# ---Maximize window---
#driver.maximize_window()
#driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.forward()

time.sleep(10)