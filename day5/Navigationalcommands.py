import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://snapdeal.com/")
driver.get("https://amazon.com")
driver.maximize_window()
driver.back()
driver.forward()
driver.refresh()
driver.quit()