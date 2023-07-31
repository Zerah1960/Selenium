import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(5)
# driver.close()
driver.back()


#
# parent_handle = driver.current_window_handle
# handles = driver.window_handles
# for handle in handles:
#     if handle != parent_handle:
#         driver.switch_to.window(handle)
#         driver.find_element(By.CSS_SELECTOR, "#Form_submitForm_EmailHomePage").send_keys("abd.com")

